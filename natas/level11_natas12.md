Level #11 go to URL and find natas11 user password

- URL: http://natas11.natas.labs.overthewire.org/
- User: natas11
- Password: D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE

After navigating to URL an html page with a form is rendered and an anchor element with the text "View sourcecode".  
Clicking on the anchor elements redirects to the source code of the php script being run by server, in summary the script is:
- declares a default array $defaultdata
- loadData function makes a copy of $defaultdata, checks if there is a 'data' cookie already set and updates $defaultdata with cookie, otherwise returns the unmodified $defaultdata
- conditional if statement checks if there is an 'bgcolor' array key in $_REQUEST and updates the value of it in the 'data' cookie
- saveData function saves json encoded (json_encode()), xor encrypted (internal function), and base64 encoded $defaultdata into 'data' cookie and sets it in the response
  
To get natas12 password an XOR encryption key is needed and then pass to loadData function a modified $defaultdata that has showpassword => 'yes'.  
Calculating the XOR key was done by executing a reverse operation of the encryption, if a ^ key = b then b ^ a = key.  
  
![[/Users/kmnj500/Desktop/Screenshot\ 2023-09-22\ at\ 10.24.29.png]]  
  
Since we already know a (json encoded $defaultdata) and b (json encoded $defaultdata after XOR operation with key).  
  
```PHP
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$cookie = "MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY=";
$a = json_encode($defaultdata);
$b = base64_decode($cookie);
$key_repeated = $a ^ $b;
```
  
The password for natas12 is YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG
