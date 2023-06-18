from imessage_reader import fetch_data
import os

def send_to_number(recipient_number, message):
    fd = fetch_data.FetchData()
    messages  = fd.get_messages()
    os.system("osascript /Users/shrey/Developer/ketchup/server/sendMessage.applescript {} {}".format(recipient_number, message))

def send_to_group(groupID, message):
    fd = fetch_data.FetchData()
    messages  = fd.get_messages()
    os.system("osascript /Users/shrey/Developer/ketchup/server/sendMessageGroup.applescript {} {}".format(groupID, message))
