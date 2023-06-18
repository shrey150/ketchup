import getpass
import sqlite3
import datetime

def get_messages(days_ago):

    user = getpass.getuser()

    con = sqlite3.connect(f"/Users/{user}/Library/Messages/chat.db")
    cur = con.cursor()

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=days_ago)

    response = cur.execute(f"""SELECT text, date, handle.id, chat.display_name
                            FROM message
                            JOIN handle ON message.handle_id = handle.ROWID
                            JOIN chat ON message.cache_roomnames = chat.room_name
                            WHERE datetime(date/1000000000 + 978307200,'unixepoch','localtime') >= '{now - delta}'
                            ORDER BY date DESC
                            """)
    
    messages = response.fetchall()

    return messages
    

