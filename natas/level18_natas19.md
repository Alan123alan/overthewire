Level #18 go to URL and find natas18 user password

- URL: http://natas18.natas.labs.overthewire.org/
- User: natas18
- Password: 8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq

After navigating to URL an html page with a form with 3 inputs and an anchor element with the text "View sourcecode" is loaded.
Clicking on the anchor elements redirects to the source code of the php script being run by server.

How do they work?
- [is_numeric](https://www.php.net/manual/es/function.is-numeric.php): checks if a variable is a number/numeric string or not.
- [$_REQUEST](https://www.php.net/manual/en/reserved.variables.request.php): associative array that contains the contents of $_GET,
  $_POST, $_COOKIE.
- [session_start](https://www.php.net/manual/en/function.session-start.php): start new or resume existing session.
- [rand](https://www.php.net/manual/es/function.rand.php): generate a random integer between a min and max(inclusive) if given.
  

```PHP
<?php

$maxid = 640; // 640 should be enough for everyone

function isValidAdminLogin() { /* {{{ */
    # checks if request associative array contains the key "username"
    if($_REQUEST["username"] == "admin") {
    /* This method of authentication appears to be unsafe and has been disabled for now. */
        //return 1;
    }

    return 0;
}
/* }}} */
function isValidID($id) { /* {{{ */
    # checks if the $id passed is a numeric value or a numeric string
    # returns true if it is and false if not
    return is_numeric($id);
}
/* }}} */
function createID($user) { /* {{{ */
    global $maxid;
    # generates a random integer between 1 and 640
    return rand(1, $maxid);
}
/* }}} */
function debug($msg) { /* {{{ */
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}
/* }}} */
function my_session_start() { /* {{{ */
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {
    if(!session_start()) {
        debug("Session start failed");
        return false;
    } else {
        debug("Session start ok");
        if(!array_key_exists("admin", $_SESSION)) {
        debug("Session was old: admin flag set");
        $_SESSION["admin"] = 0; // backwards compatible, secure
        }
        return true;
    }
    }

    return false;
}
/* }}} */
function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas19\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.";
    }
}
/* }}} */

$showform = true;
if(my_session_start()) {
    print_credentials();
    $showform = false;
} else {
    if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) {
    session_id(createID($_REQUEST["username"]));
    session_start();
    $_SESSION["admin"] = isValidAdminLogin();
    debug("New session started");
    $showform = false;
    print_credentials();
    }
}

if($showform) {
?>

<p>
Please login with your admin account to retrieve credentials for natas19.
</p>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<?php } ?>
```

Looking at the code it seems like the main possible vulnerability would be in my_session_start() and print_credentials() functions.

#### Dissecting my_session_start() function

Function starts by checking if $_COOKIE contains a the key PHPSESSID and that it is set to a numeric value or a numeric string,
if both exists it then hops to another check depending on session_start() if session started successfully "Session star ok" will print,
finally it will check if the key "admin" exists in the $_SESSION asociative array and if it doesn't it will reset the $SESSION["admin"]
to 0.

#### What is needed to print natas19 password?

That a $_SESSION is not null, that it contains the "admin" key and that it's value is equal to 1.

#### Can you modify $_SESSION from the request

Found [this](https://stackoverflow.com/questions/70896709/session-superglobals-with-postman#:~:text=1-,Is%20it%20possible%20to%20include%20or%20pass%20the%20%24_SESSION,be%20a%20huge%20security%20hole.) about setting $_SESSION from the request.
  
#### Can you keep making new sessions until one grants access as admin? 

Generate a session from 1 to 640 and check if admin access is granted by parsing response until you get `You are an admin. The credentials for the next level are:` text.

The password for natas19 is: 
8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s
