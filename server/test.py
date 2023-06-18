import db
import llm

messages = db.get_messages(days_ago=1)
print(llm.generate_topics(messages))
