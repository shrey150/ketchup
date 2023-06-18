tell application "Messages"
  set myid to "iMessage;+;chat107061102355140117"
  set mymessage to "Hello World"
  set theBuddy to a reference to chat id myid
  send mymessage to theBuddy
end tell