import requests

bot_token = ''
chat_id = ''
notification_text = 'Your notification message'

url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={notification_text}'

response = requests.get(url)

print(response.json())
