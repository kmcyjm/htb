import requests
import hashlib
import logging
import re

logging.basicConfig(level=logging.INFO)

# create a persist session so the POST request is considered
# the response to the intial GET request

# Note, however, that method-level parameters will not be persisted across requests, even if using a session. This example will only send the cookies with the first request, but not the second:

e = requests.Session()

# first get requet
r = e.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# '{"cookies": {"from-my": "browser"}}'

# A different get request which does not have the cookies set in the first request
r = e.get('https://httpbin.org/cookies')
print(r.text)
# '{"cookies": {}}'


s = requests.Session()
url = 'http://64.227.36.245:32063'

res = s.get(url)
m = re.search("<h3 align='center'>([a-zA-Z0-9]+)</h3>", res.text)
if m:
  md5str = m.group(1)
  logging.info('Hasing string ... ', md5str)
  hash = hashlib.md5(md5str.encode())
  logging.info('Sending hash ... ', str(hash))
  
  payload = hash.hexdigest()
  data = dict(hash=payload)
  res = s.post(url=url, data=data)
  if res:
    print(res.text)
