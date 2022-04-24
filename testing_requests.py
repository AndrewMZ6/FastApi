import requests as rq
import json

url = 'http://127.0.0.1:8000/todo'

resp = rq.get(url)
print(resp.text)

# console output
# {"data":[{"id":"1","Activity":"puting things in order at my folders"},{"id":"2","Activity":"make my radio access labs ready"},{"id":"3","Activity":"do some laundry already!"}]}

post_body =  json.dumps({'id':'3', 'Activity':'do some laundry already!'})
resp = rq.post(url, data =post_body)
print(resp.text)

# console output
# {"data":"successfull!"}

resp = rq.get(url)
print(resp.text)

# console output
# {"data":[{"id":"1","Activity":"puting things in order at my folders"},{"id":"2","Activity":"make my radio access labs ready"},{"id":"3","Activity":"do some laundry already!"},{"id":"3","Activity":"do some laundry already!"}]}
