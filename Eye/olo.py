import requests

res = requests.post('192.168.56.1', 7000, data={'st3': 'jim hopper'})
print(res.text)