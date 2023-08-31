Level #5 go to URL and find natas5 user password

- URL: http://natas4.natas.labs.overthewire.org/
- User: natas4
- Password: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm

### after navigating to URL an html page shows a div with following text
### "Access disallowed. You are visiting from "" while authorized users
### should come only from "http://natas5.natas.labs.overthewire.org/""
### so by using chrome browser on a mac cmd + opt + i into chrome developer tools
### then went into elements tab to inspect the html and didn't find and html comment with the password
### thought about the form embedded into page checked the payload but nothing interesting
### checked for the robots.txt file but request resulted in a 404 response
### the site had an anchor element with an href to index.php
### once the anchor element is clicked text in page changes to:
### "Access disallowed. You are visiting from 
### "http://natas4.natas.labs.overthewire.org/" while authorized users should
### come only from "http://natas5.natas.labs.overthewire.org/"
### thought about from where was index.php file pulling the value:
### http://natas4.natas.labs.overthewire.org/ 
### to append it to original message, there was no payload in the request
### it could be checking the request URL or passing a value in the headers
### the value was being passed in the "Referer" header
### since I couldn't came up with a way to modify header in the browser
### I just reassembled the request with postman
```
GET http://natas4.natas.labs.overthewire.org/index.php
Authorization: Basic bmF0YXM0OnRLT2NKSWJ6TTRsVHM4aGJDbXpuNVpyNDQzNGZHWlFt
Referer: http://natas5.natas.labs.overthewire.org/
Cookie: i__utmz=176859643.1688335721.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=176859643; __utma=176859643.1971156912.1688335721.1693192766.1693254709.55; _sm_au_c=kj48CAOz84hWp7n0Ngp21AB4Gf2A4adsbK+iM3CWK7wUgAAAAMPm6yUPmh5nn7AapBsQ8Grd5YzOmCCJqvyoJAelMeho=; _sm_au_c=kj48CADWHjGkZ3gdrB11i4JfzCk0GF+H6XJ7kKryZ4kcgAAAAP0PS2wVEMVNvCmKuRe3olZq31G36KGEqVnEoLBMY4hs=; _sm_au_c=kj48CALBE4j7Ggw/Zb6gIu7tdJjWMmDWQOmE1is0+N4IgAAAAUO8x3sW0E6MvVTNW4vBPGeA+LS0R/9RS2ExIxmUotck=; __utmb=176859643.3.10.1693254709
```

### <!--The password for natas5 is Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD-->
