import sys
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_topics(messages):
    prompt = ""

    for row_id in messages:
        text, date, handle_id, display_name = messages[row_id]
        prompt += f"{row_id}: {text}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Organize these messages into topics. For each topic, come up with a title for the topic, followed by a colon, followed by an emoji for the title, followed by a colon, followed by a comma-seperated list of message IDs."
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

        try:
            title, emoji, IDs = line.split(":")

            title = title.strip()

            IDs = [int(ID.strip()) for ID in IDs.split(",")]

            topics.append((emoji, title, IDs))
        except:
            print(line)
            sys.exit(1)

    return topics

def generate_summary(messages):

    prompt = ""

    for row_id in messages:
        text, date, handle_id, display_name = messages[row_id]
        prompt += f"{text}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Create a one-sentence summary of the following messages."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return response.choices[0].message.content

def generate_bullets(messages):

    prompt = ""

    for row_id in messages:
        text, date, handle_id, display_name = messages[row_id]
        prompt += f"{handle_id}: {text}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Create a bulleted summary of the following messages associated with the phone number, using roughly three bullets in total. Each bullet should be a complete sentence beginning on a newline with zero extra characters."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    content = response.choices[0].message.content

    return content.split("\n")
