Level #17 go to URL and find natas17 user password

- URL: http://natas17.natas.labs.overthewire.org/
- User: natas17
- Password: XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd

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
    $link = mysqli_connect('localhost', 'natas17', '<censored>');
    mysqli_select_db($link, 'natas17');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
<?php } ?>
```

SQL injection seems to be the exploit needed for this level, the only issue is that there is no obvious way to confirm results, once
injection is executed from server side, all echo functions for results are commented.

Can I also inject PHP code so that it retrieves the results of query? I didn't find how to execute php code within a string. 
How can you check a query found a result without getting a result back? you can set some delay and check the response time, sql
short circuits an `and` operation between 2 logic statements so if the first is false, the seconds doesn't get executed.

```SQL
-- something like this will instantly return if username is not found
-- and it will take 10 seconds to respond if the username is found in the table
SELECT * FROM users WHERE username="<some_username>" AND SLEEP(10);
-- this can be adapted to confirm a letter is in the password field
SELECT * FROM users WHERE username="natas18" AND password LIKE BINARY "<some_letter>" AND SLEEP(5)
```

Within the requests python module there is a property in the Response object named elapsed which shows the time delta between request
and response. More info [here](https://stackoverflow.com/questions/43252542/how-to-measure-server-response-time-for-python-requests-post-request)

  
The password for natas18 is 
8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq
