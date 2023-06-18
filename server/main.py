from fastapi import FastAPI
import db
import llm

app = FastAPI()

@app.get("/topics")
def get_topics():
    messages = db.get_messages(days_ago=1)
    topics = llm.generate_topics(messages)
    
    reponse = []
    topic_id = 0
    for emoji, title, IDs in topics:
        topic_messages_dict = {ID: messages[ID] for ID in IDs}
        summary = llm.generate_summary(topic_messages_dict)
        bullets = llm.generate_bullets(topic_messages_dict)
        topic_messages = []
        for ID in topic_messages_dict:
            text, date, handle_id, display_name = topic_messages_dict[ID]
            topic_messages.append({"groupName": display_name, "senderName": handle_id, "text": text, "timestamp": date})
        reponse.append({"id": topic_id, "emoji": emoji, "name": title, "description": summary, "messageCount": len(IDs), "summary": bullets, "updatedAt": min(topic_messages, key=lambda msg: msg.date).date, "messages": topic_messages})
        topic_id += 1
    return reponse
