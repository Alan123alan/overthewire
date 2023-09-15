Level #3 go to URL and find natas4 user password

- URL: http://natas3.natas.labs.overthewire.org/
- User: natas3
- Password: G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q 

### after navigating to URL an html page shows a div with following text
### "There is nothing on this page"
### so by using chrome browser on a mac cmd + opt + i into chrome developer tools
### then went into elements tab to inspect the html and didn't find and html comment with the password
### thought about the form embedded into page checked the payload but nothing interesting
### saw a hint online that suggested looking through the robots.txt file
### a robots.txt file contains instructions telling search engines crawlers
### which pages from your site they should or shouldn't access.
### this is done by "allowing" or "disallowing" the behaviour of crawlers
### so navigated to file http://natas3.natas.labs.overthewire.org/robots.txt
### this "disallowed" crawlers to access /s3cr3t/
### so navigated into http://natas3.natas.labs.overthewire.org/s3cr3t
### this navigated into a folder in server that stores a users.txt file
### accessed users.txt file and found:
- natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm

### <!--The password for natas4 is tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm -->
