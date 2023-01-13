### NKA 2022. RqChat API by thatOneArchUser. For enquiries, contact <nka.dev@outlook.com>

"""Handles and sends messages through RqChat."""

import requests
import datetime
import time

class MessageHandler:
    def __init__(self, username: str, client_id, *, show_timestamps: bool = False):
        self.username = username
        self.__client_id = client_id
        self.show_timestamps = show_timestamps

    def send(self, message: str):
        m = str()
        if self.show_timestamps:
            ts = datetime.datetime.now()
            ts_formatted = time.strftime("%H:%M", ts)
            m = f"[{ts_formatted}] {message}"
        else: m = message
        api_request = requests.get(f"https://rqchat.thatonearchuser.repl.co/send?username={self.username}&msg={m}&cid={self.__client_id}")
        if api_request.status_code != 200: raise RuntimeError(f"Message send failure (Status Code {api_request.status_code}): {api_request.text}")
        else: return True

    def reply(self, base_message_content: str, message: str):
        m = str()
        if self.show_timestamps:
            ts = datetime.datetime.now()
            ts_formatted = time.strftime("%H:%M", ts)
            m = f"[{ts_formatted}] > {base_message_content}: {message}"
        else: m = f"> {base_message_content}: {message}"
        api_request = requests.get(f"https://rqchat.thatonearchuser.repl.co/send?username={self.username}&msg={m}&cid={self.__client_id}")
        if api_request.status_code != 200: raise RuntimeError(f"Message send failure (Status Code {api_request.status_code}): {api_request.text}")
        else: return True
