import sqlite3
import datetime

con = sqlite3.connect("/Users/arvind/Library/Messages/chat.db")
cur = con.cursor()

def nanoseconds_in_years(years):
    # Create a timedelta object for the specified number of years
    timedelta = datetime.timedelta(days=365) * years

    # Get the total number of seconds in the timedelta
    total_seconds = timedelta.total_seconds()

    # Convert seconds to nanoseconds
    nanoseconds = total_seconds * 1e9

    return nanoseconds

# Calculate the number of nanoseconds in 31 years
year31_nanoseconds = nanoseconds_in_years(31)
current_time = datetime.datetime.now()
current_time_ns = current_time.microsecond * 1000
offset_time_ns = current_time_ns - year31_nanoseconds - (1*24*60*60*1e9)

res = cur.execute(f"SELECT text, date, handle_id FROM message WHERE is_read = 0 AND is_from_me = 0 AND text is NOT NULL AND date >= {offset_time_ns} ORDER BY date DESC")

print(res.fetchall())
