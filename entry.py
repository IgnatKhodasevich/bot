# -*- coding UTF-8 -*-
import requests


def point(event, context):
    print (event)

    if event["message"]["text"][0] == "/":
        words = event["message"]["text"].split()
        command = words[0][1:]
        if command == "echo":
            send_message(event["message"]["from"]["id"], event["message"]["text"])
        elif command == "help":
            help_text = "This is the list of my commands: "
            send_message(event["message"]["from"]["id"], help_text)
        elif command == "Hi":
            hello_text = "Hello! My name is Perseptron Bot"
            send_message(event["message"]["from"]["id"], hello_text)
        else:
            send_message(event["message"]["from"]["id"], "I don't know this command")
    else:
        words = event["message"]["text"].split(" ")
        if words[0] == "привет" or "Привет":
            send_message(event["message"]["from"]["id"], "Привет! Как тебя зовут?")
        elif words[0] == "Лиза" or "лиза" or "liza" or "Liza":
            send_message(event["message"]["from"]["id"], "Дурацкое имя :)")
            send_message(event["message"]["from"]["id"], "Лиза - дура! :) :) ;)")


def send_message(chat_id, text):

    url = "https://api.telegram.org/bot{token}/{method}".format(
        token="438752112:AAFKwbIeMjzZKvbuxnVQDu3NxBUsnh9TPD8",
        method="sendMessage"
    )
    data = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(url, data=data)
    print (r.json())


#
# def start_request():
#     url = "https://api.telegram.org/bot{token}/{method}".format(
#         token = "438752112:AAFKwbIeMjzZKvbuxnVQDu3NxBUsnh9TPD8",
#         method = "setWebhook"
#     )
#
#     data = {
#         "url": "https://jcd87krb52.execute-api.eu-west-1.amazonaws.com/vm00/7b039e45580c61bed084a87d1d2e4b25"
#     }
#     r = requests.post(url, data=data)
#     print (r.json())
# if __name__ == "__main__":
#     start_request()
