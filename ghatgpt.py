import requests, json

input_text = input('What would you like to ask ChatGPT? : ')

keyFile = open('key.txt', 'r')

key = keyFile.readline(0)

headers = {
    'Content-Type': 'application/json'
    'Authorization': f'Bearer {key}'
}

data = {
    'prompt' : input_text,
    'max_toxens' : 100,
    'tempurature' : .5
}

response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', data = data, headers = headers)

response_data = json.loads(response.text)
if response.status_code == 200:
    print(response_data['choices'][0]['text'])

else:
    print(f'Status Code: {response.status_code}')
    print(f'Error: {response_data['error']['message']}')