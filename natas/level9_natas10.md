Level #9 go to URL and find natas10 user password

- URL: http://natas9.natas.labs.overthewire.org/
- User: natas9
- Password: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd

After navigating to URL an html page with a form is rendered and an anchor element with the text "View sourcecode".  
Clicking on the anchor elements redirects to the source code of the php script being run by server, in summary the script is:
- getting the value submitted in the form
- passing the value to do a grep command via the php [passthru()](https://www.php.net/manual/en/function.passthru.php) function 
  
By looking at the direct interpolation of the value and the grep command I thought some simple injection could be done so my  
input was:  
  
```Bash
*; cat /etc/natas_webpass/natas10; rm
```
  
The password for natas10 is D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE
