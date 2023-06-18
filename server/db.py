import getpass
import sqlite3
import datetime

user = getpass.getuser()
con = sqlite3.connect(f"/Users/{user}/Library/Messages/chat.db")
cur = con.cursor()


def get_messages(days_ago):

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=days_ago)

    response = cur.execute(f"""SELECT text, date, handle.id, chat.display_name
                            FROM message
                            JOIN handle ON message.handle_id = handle.ROWID
                            JOIN chat ON message.cache_roomnames = chat.room_name
                            WHERE datetime(date/1000000000 + 978307200,'unixepoch','localtime') >= '{now - delta}'
                            AND text is NOT NULL
                            ORDER BY date DESC
                            """)
    
    messages = response.fetchall()

    return messages

def get_unread_messages(days_ago):

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=days_ago)

    response = cur.execute(f"""SELECT text, date, handle.id, chat.display_name
                            FROM message
                            JOIN handle ON message.handle_id = handle.ROWID
                            JOIN chat ON message.cache_roomnames = chat.room_name
                            WHERE datetime(date/1000000000 + 978307200,'unixepoch','localtime') >= '{now - delta}'
                            AND is_read = 0
                            AND is_from_me = 0
                            AND text is NOT NULL
                            ORDER BY date DESC
                            """)
    
    messages = response.fetchall()

    return messages
