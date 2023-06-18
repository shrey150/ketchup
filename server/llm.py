import sys
import openai
from dotenv import load_dotenv
import os
from contacts import ContactInfo

load_dotenv()

contacts = ContactInfo().get()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_topics(messages):
    prompt = ""

    print(messages)

    for row_id in messages:
        text, date, handle_id, display_name, guid = messages[row_id]
        prompt += f"{row_id}: {text}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Organize these messages into topics. For each topic, come up with a title for the topic, followed by a colon, followed by an emoji for the title, followed by a colon, followed by a category for the topic (either work, personal, or other), followed by a colon, followed by a comma-seperated list of message IDs."
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
            title, emoji, category, IDs = line.split(":")

            title = title.strip()
            emoji = emoji.strip()

            IDs = [int(ID.strip() ) for ID in filter(bool, IDs.split(","))]

            topics.append((emoji, title, category, IDs))
        except:
            print(line)
            sys.exit(1)

    return topics

def generate_summary(messages):
    prompt = ""

    for row_id in messages:
        text, date, handle_id, display_name, guid = messages[row_id]
        prompt += f"{text}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.1,
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

def generate_response(messages):
    prompt = ""

    for row_id in messages:
        text, date, handle_id, display_name, guid = messages[row_id]
        prompt += f"{text}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.1,
        messages=[
            {
                "role": "system",
                "content": "Create a short response to the following messages in a conversation."
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
        text, date, handle_id, display_name, guid = messages[row_id]

        if handle_id in contacts:
            name = contacts[handle_id]['name']
        else:
            name = handle_id

        prompt += f"{name}: {text}\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0.1,
        messages=[
            {
                "role": "system",
                "content": "Create a bulleted summary of the following messages associated with the phone number, using roughly three bullets in total. Each bullet should be a complete sentence beginning on a newline with zero extra characters. Do not include the bullet point characters themselves."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    content = response.choices[0].message.content

    return content.split("\n")
