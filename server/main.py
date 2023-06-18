from typing import Any, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import db
import llm
import message_sender
from pprint import pprint
from contacts import ContactInfo

app = FastAPI()
app.debug = True
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/ping')
def ping():
    return { 'pong' }

contacts =  ContactInfo().get()

class Input(BaseModel):
    identifiers: List[str]

@app.post("/api/contact-info")
def get_contact_info(input: Input):
    identifiers = input.identifiers
    return [contacts[identifier] for identifier in identifiers]

@app.get("/api/unread-count")
def get_unread_count():
    return db.count_unread_messages(days_ago=1)

@app.get("/api/topics")
def get_topics():
    print('Fetching messages')
    messages = db.get_messages(days_ago=1)
    print('Generating topics')
    topics = llm.generate_topics(messages)
    print('Got topics!')
    pprint(topics)
    response = []
    topic_id = 0
    for emoji, title, IDs in topics:
        topic_messages_dict = {ID: messages[ID] for ID in IDs}
        print('Generating summary')
        summary = llm.generate_summary(topic_messages_dict)
        print('Generating bullets')
        bullets = llm.generate_bullets(topic_messages_dict)
        text_response = llm.generate_response(topic_messages_dict)
        print('Generating text response')
        topic_messages = []
        dates = []
        for ID in topic_messages_dict:
            text, date, handle_id, display_name, guid = topic_messages_dict[ID]
            dates.append(date)
            topic_messages.append({"groupName": display_name, "senderName": handle_id, "text": text, "timestamp": date})
        response.append({"id": topic_id, "emoji": emoji, "name": title, "description": summary, "messageCount": len(IDs), "summary": bullets, "textResponse": text_response, "updatedAt": min(dates), "messages": topic_messages})
        topic_id += 1
    print('Returning topics')
    return response

@app.get("/api/topics/by-chat")
def get_topics_by_chat():
    print('Fetching messages')

    messages = db.get_messages(days_ago=1)

    print('Generating topics')

    chats = db.organize_by_chat(messages)
    topics = []

    for chat_name in chats:
        topics.extend(llm.generate_topics(chats[chat_name]))

    print('Got topics!')
    pprint(topics)
    response = []
    topic_id = 0
    for emoji, title, IDs in topics:
        topic_messages_dict = {ID: messages[ID] for ID in IDs}
        print('Generating summary')
        summary = llm.generate_summary(topic_messages_dict)
        print('Generating bullets')
        bullets = llm.generate_bullets(topic_messages_dict)
        print('Generating text response')
        text_response = llm.generate_response(topic_messages_dict)
        topic_messages = []
        dates = []
        for ID in topic_messages_dict:
            text, date, handle_id, display_name, guid = topic_messages_dict[ID]
            dates.append(date)
            topic_messages.append({"groupName": display_name, "senderName": handle_id, "text": text, "timestamp": date})
        response.append({"id": topic_id, "emoji": emoji, "name": title, "description": summary, "messageCount": len(IDs), "summary": bullets, "textResponse": text_response, "updatedAt": min(dates), "messages": topic_messages})
        topic_id += 1
    print('Returning topics')
    return response

@app.get("/api/topics/unread")
def get_unread_messages():
    print('Fetching messages')
    messages = db.get_unread_messages(days_ago=1)
    print('Generating topics')
    topics = llm.generate_topics(messages)
    print('Got topics!')
    pprint(topics)
    response = []
    topic_id = 0
    for emoji, title, IDs in topics:
        topic_messages_dict = {ID: messages[ID] for ID in IDs}
        print('Generating summary')
        summary = llm.generate_summary(topic_messages_dict)
        print('Generating bullets')
        bullets = llm.generate_bullets(topic_messages_dict)
        print('Generating text response')
        text_response = llm.generate_response(topic_messages_dict)
        topic_messages = []
        dates = []
        for ID in topic_messages_dict:
            text, date, handle_id, display_name, guid = topic_messages_dict[ID]
            dates.append(date)
            topic_messages.append({"groupName": display_name, "senderName": handle_id, "text": text, "timestamp": date})
        response.append({"id": topic_id, "emoji": emoji, "name": title, "description": summary, "messageCount": len(IDs), "summary": bullets, "textResponse": text_response, "updatedAt": min(dates), "messages": topic_messages})
        topic_id += 1
    print('Returning topics')
    return response

@app.post("/api/send-message")
def send_message(input):
    print("Attempting to send message")
    message = input["message"]
    roomName = input["roomName"]
    if "chat" in roomName:
        py_imessage.send_to_group(roomName, message)
    else:
        py_imessage.send_to_number(roomName, message)
    print("Sent message")

def my_middleware(app):
    def middleware(environ, start_response):
        # Call the original app to get the response
        response = app(environ, start_response)

        # Add custom headers to the response
        headers = [('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Headers', '*'), ("X-foo", "bar")]
        new_response = []
        for name, value in response:
            if name.lower() != 'content-length':
                new_response.append((name, value))
        new_response.extend(headers)

        return new_response

    return middleware

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
