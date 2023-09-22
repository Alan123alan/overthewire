Level #10 go to URL and find natas11 user password

- URL: http://natas10.natas.labs.overthewire.org/
- User: natas10
- Password: D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE

After navigating to URL an html page with a form is rendered and an anchor element with the text "View sourcecode".  
Clicking on the anchor elements redirects to the source code of the php script being run by server, in summary the script is:
- getting the value submitted in the form through the PHP [$_REQUEST](https://www.php.net/manual/en/reserved.variables.request.php)
- validating that the value submitted through the input doesn't include [;|&] with [preg_match()](https://www.php.net/manual/en/reserved.variables.request.php)
- passing the value to do a grep command via the php [passthru()](https://www.php.net/manual/en/function.passthru.php) function if valid
  
The direct injection of ; used inprevious excercise is not possible this time, checked some exploits regarding preg_match  
but none were effective, ended up just looking for some random char at /etc/natas_webpass/natas11  
input was:  
  
```Bash
p /etc/natas_webpass/natas11 
a /etc/natas_webpass/natas11 
```
  
looking for 'c' in both files showed results just from dictionary.txt.  
looking for 'a' in both files resulted in the password.  
   
The password for natas11 is 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg 
