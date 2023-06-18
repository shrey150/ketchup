import openai
openai.api_key="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"

def generate_topics(messages):

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Organize these messages into topics. For each topic, respond with a topic title, followed by a list of message IDs on a newline."
            },
            {
                "role": "user",
                "content": str(messages)
            }
        ],
    )

    return response
