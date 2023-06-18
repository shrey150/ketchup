import db
import llm

messages = db.get_messages(days_ago=1)
topics = llm.generate_topics(messages)

for emoji, title, IDs in topics:

    print(f"{emoji} {title}")

    summary = llm.generate_summary({ID: messages[ID] for ID in IDs})
    print(summary)
    print()
