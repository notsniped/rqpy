# Imports
import rqpy, time
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
class PrefixCommandListener:
    """Handles commands in the bot client."""

    def start(self):
        """Starts listening for commands"""

        latest_message_cached = ""

        def wait_for_message():
            latest_message_context = latest_message.split(": ")
            latest_message_author = latest_message_context[0]
            latest_message_content = latest_message_context[1]
            if latest_message_author == username: return
            print(latest_message_content)
            if str(latest_message_content) == "/say_hi": 
                ctx.send("Hellow uwu")
                latest_message_cached = ""
                return
            elif str(latest_message_content) == "/help": 
                ctx.send("Help list:\n    /help (this command): sends help\n    /say_hi: makes the bot say hi back to you")
                latest_message_cached = ""
                return
            else:
                latest_message_cached = "" 
                return

        while True:
            latest_message = channel.get_message()
            if latest_message != latest_message_cached or len(latest_message) != 0: 
                latest_message_cached = latest_message
                wait_for_message()
            else: pass

            # NOTE:
            # Avoid using latest message cache for 
            # triggering bot commands. Doing this 
            # may lead to multiple commands being
            # false-invoked at the same time. Use 
            # direct message cache instead.

# Running Command Listener
commands = PrefixCommandListener()
commands.start()
