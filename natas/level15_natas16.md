Level #15 go to URL and find natas16 user password

- URL: http://natas15.natas.labs.overthewire.org/
- User: natas15
- Password: TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB

After navigating to URL an html page with a form with 2 inputs and an anchor element with the text "View sourcecode" is loaded.
Clicking on the anchor elements redirects to the source code of the php script being run by server.
  

```PHP
<?php
/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas15', '<censored>');
    mysqli_select_db($link, 'natas15');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>
```

The query selects everything from database where the `username` passed by the user is found, this should retrieve the password too.  
Main issue is that the result of the query is not echoed to the user, just some hardcoded text. By adding a `debug` parameter to 
the request allows us to see the query being assembled from the template + user input.  
  
A script in Python could be useful to make multiple requests, sending an injected query that checks if a `password` starts with a given
substring.  
  
The password for natas16 is 
TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V
