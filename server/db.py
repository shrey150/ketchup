import getpass
import sqlite3
import datetime

user = getpass.getuser()
con = sqlite3.connect(f"/Users/{user}/Library/Messages/chat.db", check_same_thread=False)
cur = con.cursor()

def count_unread_messages(days_ago):

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=days_ago)

    response = cur.execute(f"""SELECT COUNT(*) as unread_count
                                FROM message
                                JOIN handle ON message.handle_id = handle.ROWID
                                JOIN chat ON message.cache_roomnames = chat.room_name
                                WHERE datetime(date/1000000000 + 978307200,'unixepoch','localtime') >= '{now - delta}'
                                AND is_read = 0
                                AND is_from_me = 0
                                AND text is NOT NULL
                                """)
    return response.fetchone()[0]

def organize_by_chat(messages):

    chats = {}

    for row_id in messages:
        text, date, handle_id, display_name, guid = messages[row_id]
        if display_name not in chats:
            chats[display_name] = {}
        
        chats[display_name][row_id] = messages[row_id]
    
    return chats

def get_messages(days_ago):

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=days_ago)

    response = cur.execute(f"""SELECT message.ROWID, text, date, handle.id, chat.display_name, chat.guid
                            FROM message
                            JOIN handle ON message.handle_id = handle.ROWID
                            JOIN chat ON message.cache_roomnames = chat.room_name
                            WHERE datetime(date/1000000000 + 978307200,'unixepoch','localtime') >= '{now - delta}'
                            AND text is NOT NULL
                            ORDER BY date DESC
                            """)
    
    messages = {}

    for row_id, text, date, handle_id, display_name, guid in response.fetchall():
        messages[row_id] = (text, date, handle_id, display_name, guid)

    return messages

def get_unread_messages(days_ago):

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=days_ago)

    response = cur.execute(f"""SELECT message.ROWID, text, date, handle.id, chat.display_name, chat.guid
                            FROM message
                            JOIN handle ON message.handle_id = handle.ROWID
                            JOIN chat ON message.cache_roomnames = chat.room_name
                            WHERE datetime(date/1000000000 + 978307200,'unixepoch','localtime') >= '{now - delta}'
                            AND is_read = 0
                            AND is_from_me = 0
                            AND text is NOT NULL
                            ORDER BY date DESC
                            """)

    messages = {}

    for row_id, text, date, handle_id, display_name, guid in response.fetchall():
        messages[row_id] = (text, date, handle_id, display_name, guid)

    return messages
