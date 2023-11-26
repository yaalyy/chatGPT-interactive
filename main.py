from openai import AuthenticationError, APIConnectionError
from config import prompt
from chat_session import ChatSession


if __name__ == "__main__":
    if len(prompt) == 0:
        newSession = ChatSession()
    else:
        newSession = ChatSession(prompt=prompt)

    try:
        newResponse = newSession.start()
        print(">>" + newResponse.choices[0].message.content)
        while True:
            print(">>", end="")
            newResponse = newSession.send(input())
            print(">>" + newResponse.choices[0].message.content)
    except AuthenticationError:
        print("Authentication Error, please check api-key")
    except APIConnectionError:
        print("Network Connection error")



