Level #6 go to URL and find natas6 user password

- URL: http://natas5.natas.labs.overthewire.org/
- User: natas5
- Password: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD

### after navigating to URL an html page shows a div with following text
### "Access disallowed. You are not logged in"
### so by using chrome browser on a mac cmd + opt + i into chrome developer tools
### then went into elements tab to inspect the html and didn't find and html comment with the password
### thought about the form embedded into page checked the payload but nothing interesting
### checked for the robots.txt file but request resulted in a 404 response
### the site had an anchor element with an href to index.php
### loading the site just loads the same requests over an over
- natas5.natas.labs.overthewire.org
- jquery-ui.css
- wechall.css
- jquery-1.9.1.js
- jquery-ui.js
- wechall-data.js
- wechall.js
- wechall.gif
### not a way to trigger a different request like with previous natas game
### looked at the request in more detail and found that request for
### natas5.natas.labs.overthewire.org has the header -> Cookie : loggedin=0
### since I couldn't came up with a way to modify header in the browser
### I just reassembled the request with postman changing header to ->
### Cookie : loggedin1
```
### <!--The password for natas6 is fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR -->
