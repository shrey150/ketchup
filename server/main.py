from waitress import serve
from flask import Flask, current_app
from flask_cors import CORS
import db
import llm
from pprint import pprint

app = Flask(__name__)
CORS(app)
app.debug = True

@app.get("/api/topics")
def get_topics():
    print('Fetching messages')
    messages = db.get_messages(days_ago=1)
    print('Generating topics')
    topics = llm.generate_topics(messages)
    print('Got topics!')
    pprint(topics)
    reponse = []
    topic_id = 0
    for emoji, title, IDs in topics:
        topic_messages_dict = {ID: messages[ID] for ID in IDs}
        summary = llm.generate_summary(topic_messages_dict)
        bullets = llm.generate_bullets(topic_messages_dict)
        topic_messages = []
        dates = []
        for ID in topic_messages_dict:
            text, date, handle_id, display_name = topic_messages_dict[ID]
            dates.append(date)
            topic_messages.append({"groupName": display_name, "senderName": handle_id, "text": text, "timestamp": date})
        reponse.append({"id": topic_id, "emoji": emoji, "name": title, "description": summary, "messageCount": len(IDs), "summary": bullets, "updatedAt": min(dates), "messages": topic_messages})
        topic_id += 1
    return reponse


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
    serve(my_middleware(app), host='0.0.0.0', port=8000)
