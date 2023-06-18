import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_topics(messages):

    prompt = ""

    for row_id, text, date, handle_id, display_name in messages:
        prompt += f"<{row_id}> {handle_id}: {text}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Organize these messages into topics. For each topic, respond with a topic title, followed by a newline, followed by a comma-seperated list of message IDs."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    content = response.choices[0].message.content
