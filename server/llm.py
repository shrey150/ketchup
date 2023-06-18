import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_topics(messages):

    prompt = ""

    for row_id, text, date, handle_id, display_name in messages:
        prompt += f"{row_id}: {text}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Organize these messages into topics. For each topic, respond with a topic title, followed by a colon, followed by a comma-seperated list of message IDs."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    lines = response.choices[0].message.content.split("\n")
    topics = []

    for line in lines:
        if not line: continue

        title, IDs = line.split(":")

        title = title.strip()

        IDs = [int(ID.strip()) for ID in IDs.split(",")]

        topics.append((title, IDs))
    
    return topics
