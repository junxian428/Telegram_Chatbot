import requests

bot_token = ''
chat_id = '-'
message_text = 'my sample text'

url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
params = {
    'chat_id': chat_id,
    'text': message_text
}

response = requests.post(url, params=params)
print(response.json())
