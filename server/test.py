import db
import llm

messages = db.get_messages()
print(llm.generate_topics(messages))
