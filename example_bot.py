# Imports
import rqpy
import time
from rqpy.authorization import register
from rqpy.authorization import UserClient
from rqpy.messages import MessageHandler
from rqpy.chat import ChatListener

# Bot Config
username = ""
password = ""

# Variables
client = UserClient()
client_id = str()
try: client_id = client.login(username, password)
except SystemExit: client_id = register(username, password)
print(f"Client id: {client_id}")
ctx = MessageHandler(username, client_id)
channel = ChatListener()

# Commands
def command_listener():
    """Handles commands in the bot client."""
    latest_message_cached = ""
    while True:
        latest_message = channel.get_message()
        if latest_message == latest_message_cached or len(latest_message) == 0: pass
        else: latest_message_cached = latest_message

        # NOTE:
        # Avoid using latest message cache for 
        # triggering bot commands. Doing this 
        # may lead to multiple commands being
        # false-invoked at the same time. Use 
        # direct message cache instead.

        if "/say_hi" in str(latest_message): 
            ctx.send("Hellow uwu")
            latest_message_cached = ""
        elif "/help" in str(latest_message): 
            ctx.send("Help list:\n    /help (this command): sends help\n    /say_hi: makes the bot say hi back to you")
            latest_message_cached = ""
        else: pass

# Running Command Listener
command_listener()
