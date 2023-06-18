from imessage_reader import fetch_data
import os

RECIPIENT_NUMBER = "+17148031554" # I suggest adding yours initially to test
MESSAGE = "'Sent from python!'"

fd = fetch_data.FetchData()
messages  = fd.get_messages()
os.system("osascript sendMessage.applescript {} {}".format(RECIPIENT_NUMBER, MESSAGE))