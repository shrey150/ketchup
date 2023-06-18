from imessage_reader import fetch_data
import os

def send_to_number(recipient_number, message):
    fd = fetch_data.FetchData()
    messages  = fd.get_messages()
    os.system("osascript sendMessage.applescript {} {}".format(recipient_number, message))

def send_to_group(groupID, message):
    fd = fetch_data.FetchData()
    messages  = fd.get_messages()
    os.system("osascript sendMessageGroup.applescript {} {}".format(groupID, message))


SEND_TO_GROUP = "chat107061102355140117"
SEND_TO_NUM = "+17148031554"
RECIPIENT_ID_NUM = "'iMessage;+;" + SEND_TO_NUM + "'"
RECIPIENT_ID_GROUP = "'iMessage;+;" + SEND_TO_GROUP + "'"
MESSAGE = "'test message from python'"

send_to_number(RECIPIENT_ID_NUM, MESSAGE)
send_to_group(RECIPIENT_ID_GROUP, MESSAGE)