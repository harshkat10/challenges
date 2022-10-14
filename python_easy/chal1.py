import requests
from requests.auth import HTTPBasicAuth
import base64
s="admin123"
sb=s.encode("ascii")
bs=base64.b64encode(sb)
cookie_value=bs.decode("ascii")
cookies = {"session_id" :  "cookie_value" }
response = requests.get('http://localhost:8080/login', auth = HTTPBasicAuth('Kit', 'Kat'), cookies=cookies)

print(response)
