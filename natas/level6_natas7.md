Level #6 go to URL and find natas7 user password

- URL: http://natas6.natas.labs.overthewire.org/
- User: natas6
- Password: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR 

After navigating to URL an html page shows a form with an input  
and a submit button, there is also an anchor with "View sourcecode" text.  
Started by clicking on anchor element and was redirected to some php code  
that showed the validation process of the form submitted.  
  
The first things to focus on are the unfamiliar ones:
- What is $_POST? follow **[this](https://www.php.net/manual/es/reserved.variables.post.php)** for an answer
- Is array_key_exists() built in or user defined? find answer [here](https://www.php.net/manual/en/function.array-key-exists.php)
- What is an .inc file for php? **[this](https://stackoverflow.com/questions/7129842/what-is-an-inc-and-why-use-it)** basically tells you what the vulnerability is  
  
Solution was to directly access the .inc file by navigating to http://natas6.natas.labs.overthewire.org/includes/secret.inc  
  
The password for natas7 is jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
