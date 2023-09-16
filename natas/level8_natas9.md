Level #8 go to URL and find natas9 user password

- URL: http://natas8.natas.labs.overthewire.org/
- User: natas8
- Password: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

After navigating to URL an html page with a form is rendered and an anchor element with the text "View sourcecode"  
Clicking on the anchor elements redirects to the source code of the php script being run by server, in summary the script is:
- base 64 encoding the secret posted by submitting the form with php [base64_encode()](https://www.php.net/manual/es/function.base64-encode.php) function
- reversing the string with php [strrev()](https://www.php.net/manual/es/function.strrev.php) function 
- converting the reversed string to a hexadecimal string with php [bin2hex()](https://www.php.net/manual/es/function.bin2hex.php) function
- comparing the result of previous encoding/encryption against $encodedSecret which value is "3d3d516343746d4d6d6c315669563362"  
  
The most obvious process to follow was to inverse the process to decode $encodedSecret and submit the value through the form.  
- reverting the output of bin2hex php function, luckily there is a php function that does it [hex2bin()](https://www.php.net/manual/es/function.hex2bin.php)
- reverting the output of strrev() php function, this can be done  by applying again the strrev function
- decoding the base 64 encoded string with [base64_decode()](https://www.php.net/manual/es/function.base64-decode.php) php function  
  
Used an online [PHP interpreter](https://paiza.io/projects/zFTFz7CrQFx2HMYF_AE5LQ)  
  
```PHP
<?php
// Your code here!
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
echo base64_decode(strrev(hex2bin($encodedSecret)));
?>
```  
Output: oubWYf2kBq  
  
The password for natas9 is Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd
