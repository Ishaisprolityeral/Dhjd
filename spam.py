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
    r = requests.post('OTQ1MjQ2MTMyMzg3MzM2MjIy.GXhdLM.qUiPkNOCEzGFT4-wKVTe3R5nn3PLO6ZXNo1pFc', data=payload, headers=header)
  
