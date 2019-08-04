import requests
from req import RequestBuilder, RequestBuilderEncoder
import json


r = RequestBuilder()

#valid request
valid_req = RequestBuilderEncoder().encode(r)
payload = json.loads(valid_req)
res = requests.post('http://localhost:5000/validate_request', json=payload)
print(res.status_code)

#invalid request
invalid_req = RequestBuilderEncoder().encode(r.get_invalid_request())
payload = json.loads(invalid_req)
res = requests.post('http://localhost:5000/validate_request', json=payload)
print(res.status_code)

#shutdown server
res = requests.post('http://localhost:5000/shutdown')
print(res)




