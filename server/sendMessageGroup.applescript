on run {targetID, targetMessage}
    tell application "Messages"
        set myid to targetID
        set mymessage to targetMessage
        set theBuddy to a reference to chat id myid
        send mymessage to theBuddy
    end tell
end run