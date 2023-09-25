import openai
from config import api_key,prompt
from chat_session import ChatSession
if __name__ == "__main__":
    openai.api_key = api_key
    
    if len(prompt) == 0:
        newSession = ChatSession()
    else:
        newSession = ChatSession(prompt=prompt)
    
    try:
        #print(">>",end="")
        newResponse=newSession.start()
        print(">>"+newResponse['choices'][0]['message']['content'])
        while True:
            print(">>",end="")
            newResponse = newSession.send(input())
            print(">>"+newResponse['choices'][0]['message']['content'])
    except openai.error.AuthenticationError:
        print("Authentication Error, please check api-key")
    except TypeError:
        print("No response")