ModelSection = "gpt-3.5-turbo"
prompt = ""

api_key = "sk-xxxx"  # !!!!!!! api-key to access OpenAI. DO NOT PUSH ANY KEY HERE ON GIT    !!!!!!!

# model parameters below     reference: https://platform.openai.com/docs/api-reference/chat/create
Temperature = 1  # default to 1
Top_p = 1  # default to 1
Stop_sequences = []  # default to empty
# Max_tokens = 1000   #default to infinite
Presence_penalty = 0  # default to 0
Frequency_penalty = 0  # default to 0

sensitiveWordList = ["GPT", "ChatGPT", "OpenAI", "模型", "gpt", "chat", "chatgpt"]  # 敏感词设定

log_save_directory = "./logs"  # format:  /path/to/save
