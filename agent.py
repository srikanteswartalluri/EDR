import requests

payload = {
    "AGENT_ID": "1",

    "MD5": "abcd12344",

    "SHA2": "sdafbasdf234r32",

    "Unix_Time": 22122018,

    "Filename": "testfile",

    "Filepath": "/path",

    "File_Size": 20,

    "Malicious": False
}
headers = {'content-type': 'application/json'}
res = requests.post('http://localhost:5000/validate_request', json=payload)
print(res.status_code)
