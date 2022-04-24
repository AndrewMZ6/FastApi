import requests as rq
import json

url = 'http://127.0.0.1:8000/todo'

resp = rq.get(url)
print(resp.text)

post_body =  json.dumps({'id':'3', 'Activity':'do some laundry already!'})
resp = rq.post(url, data =post_body)
print(resp.text)

resp = rq.get(url)
print(resp.text)