### NKA 2022. RqChat API by thatOneArchUser. For enquiries, contact <nka.dev@outlook.com>

"""Fetches messages from RqChat's servers."""

import requests

class ChatListener:
    def __init__(self):
        print("Listening into RqChat servers.")

    def get_all_messages(self):
        api_request = requests.get("https://rqchat.thatonearchuser.repl.co/fetchall")
        if api_request.status_code != 200: raise RuntimeError(f"Message fetch failure (Status Code {api_request.status_code}): {api_request.text}")
        else: return api_request.text

    def get_message(self):
        api_request = requests.get("https://rqchat.thatonearchuser.repl.co/getlatest")
        if api_request.status_code != 200: raise RuntimeError(f"Message fetch failure (Status Code {api_request.status_code}): {api_request.text}")
        else: return api_request.text
