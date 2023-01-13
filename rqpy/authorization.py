### NKA 2022. RqChat API by thatOneArchUser. For enquiries, contact <nka.dev@outlook.com>

"""Manages client authorization in RqChat."""

# Imports
import requests

# Functions
def register(username: str, password: str):
    """
    Registers a new user in RqChat with the specified username and password.

    Returns a unique client id for further authorization.
    """
    if " " in username: raise ValueError("Username may not contain spaces")
    if " " in password: raise ValueError("Password may not contain spaces")
    api_receive = requests.get(f"https://rqchat.thatonearchuser.repl.co/register?username={username}&password={password}")
    if api_receive.status_code == 200:
        client_id = api_receive.text
        return client_id
    else: raise SystemExit(f"API request returned status code {api_receive.status_code}: {api_receive.text}")

class UserClient:
    """Makes a new user client object"""
    def __init__(self):
        api_check = requests.get("https://rqchat.thatonearchuser.repl.co/")
        if api_check.status_code != 200:
            if api_check.status_code == 404: raise SystemExit(f"API connection failed (Status Code {api_check.status_code}): The RqChat API is currently down, try again later.")
            else: raise SystemExit(f"API connection failed (Status Code {api_check.status_code}): The RqChat API is currently experiencing issues or may be offline, try again later.")
        else: print("Successfully connected to RqChat API!")
        self.__client_id = str()

    def login(self, username: str, password: str):
        """
        Logs into the RqChat API with a specified username and password.
        
        Returns a unique client id for further authorization.
        Raises `SystemExit` if there was a failure while logging in.
        """
        if " " in username: raise ValueError("Username may not contain spaces")
        if " " in password: raise ValueError("Password may not contain spaces")
        api_receive = requests.get(f"https://rqchat.thatonearchuser.repl.co/login?username={username}&password={password}")
        if api_receive.status_code == 200:
            self.__client_id = api_receive.text
            return self.__client_id
        else: raise SystemExit(f"API login failed (Status Code {api_receive.status_code}): {api_receive.text}")
