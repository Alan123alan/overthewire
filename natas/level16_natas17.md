Level #16 go to URL and find natas17 user password

- URL: http://natas16.natas.labs.overthewire.org/
- User: natas16
- Password: TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V

After navigating to URL an html page with a form with 2 inputs and an anchor element with the text "View sourcecode" is loaded.
Clicking on the anchor elements redirects to the source code of the php script being run by server.
  

```PHP
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}
?>
```

What does it do:
- [preg_match](https://www.php.net/manual/en/function.preg-match.php) performs a regular expression match
- [passthru](https://www.php.net/manual/en/function.passthru.php) runs an external program, specified in the first parameter. It prints everything output by that program to the screen

According to some posts online `preg_match()` is commonly bypassed by using multiline inputs, because pregmatch only tries to match the first line.  
The easiest way to make the payload multiline was by making it a multiline JSON.

```JSON
{
    "needle": "some stuff '",
    "search": "submit"
}
```

Now that we can bypass `preg_match()` a way to search for strings in /etc/natas_webpass/natas17 is needed, so injected some code into 
the `passthru()` function.

```JSON
{
    "needle": "1\" \"/etc/natas_webpass/natas17",
    "search": "submit"
}
```

  
The password for natas17 is 
