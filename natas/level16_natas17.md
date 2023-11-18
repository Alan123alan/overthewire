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

According to some [posts](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp) online `preg_match()` is commonly bypassed by using multiline inputs, because pregmatch only tries to match 
the first line. **ERROR** This only works if regex has it's start delimited with `^` otherwise this bypass wont work.  

Another common bypass is to pass preg_match a valid very large input, but this won't work for this specific case.

Searched for a way to execute a grep inside another grep command, eventually stumbled  
upon this [article](https://tecadmin.net/difference-between-parameter-expansion-and-command-substitution-in-bash/#:~:text=The%20%24()%20syntax%20in%20Bash,assign%20it%20to%20a%20variable.).  

##### Notes (testing in my local machine)

If you grep for a pattern and it doesn't exist in the search destination it will return nothing.
```Shell
    grep -e kkqPazSJBmrmU7UQJv17MHk1PGC4DxZMEP level13_natas14.md
```
If you grep as a pattern the result of a grep command substitution that returns nothing the parent grep
will choke.
```Shell
    grep -i $(grep -e kkqPazSJBmrmU7UQJv17MHk1PGC4DxZMEP level13_natas14.md) level14_natas15.md
```
If you grep as a pattern the result of a grep command substitution but the parent grepped file doesn't contain
the pattern, it will throw `grep: <pattern>: No such file or`.
```Shell
    #result of a grep command substitution
    echo $(grep -e genRandomString level13_natas14.md) #outputs: genRandomString
    #parent grepped file does not contain the pattern: genRandomString
    grep -i $(grep -e genRandomString level13_natas14.md) level14_natas15.md #outputs: grep: genRandomString: No such file or directory
```
If you grep as a pattern the result of a grep command substitution and the parent grepped file contains the
pattern result it will display the match in the parent grepped file.
```Shell
#result of a grep command substitution
echo $(grep -e qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP level13_natas14.md) #outputs: qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP
#parent grep takes qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP as pattern
grep -i $(grep -e qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP level13_natas14.md) level14_natas15.md #outputs: - Password: qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP
```
##### Notes(testing overthewire natas16 page behavior)

When the grep command substitution retrieves a result it will supposedly be the whole password and then the parent pattern won't find the password pattern in the grepped file, showing as a result an empty output. On the other hand if grep command substitution returns nothing then the parent grep will grep for "" pattern and as a result it will show all the words contained in grepped file.

In other words:
- if grep command substitution returns the password output is empty
- if grep command substitution returns nothing output is the file contents

With this we can extract the password by checking only if output is empty, to make the check easier add
a word that is confirmed to be in the dictionary file and that only retrieves itself when matched by grep.

Word chosen: Englishing.

Sometimes the outer grep chokes, [here](https://unix.stackexchange.com/questions/700725/how-to-grep-the-results-plural-of-another-command) is a stack exchange question about using command substitution nested in a grep.


  
The password for natas17 is 
XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd