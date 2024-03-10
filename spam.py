import requests

payload = {
    'content': 'pandaborns1968'
}

header = {
    'authorization': 'https://discord.com/channels/@me/1210205528454594560'
}

for i in range(1000):
    payload = {
        'content': i
    }
    r = requests.post('', data=payload, headers=header)
  
