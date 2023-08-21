Level #3 go to URL and find natas3 user password

- URL: http://natas2.natas.labs.overthewire.org/
- User: natas2
- Password: h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7 

### after navigating to URL an html page shows a div with following text
### "There is nothing on this page"
### so by using chrome browser on a mac cmd + opt + i into chrome developer tools
### then went into elements tab to inspect the html and didn't find and html comment with the password
### thought about the form embedded into page checked the payload but nothing interesting
### saw a hint online that suggested focusing on the file paths, only file path in page was the image path "files/pixel.png"
### started by checking file/ folder and found 2 files the pixel.png and users.txt
### accessed users.txt file and found:
- username:password
- alice:BYNdCesZqW
- bob:jw2ueICLvT
- charlie:G5vCxkVV3m
- natas3:G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
- eve:zo4mJWyNj2
- mallory:9urtcpzBmH

### <!--The password for natas3 is G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q-->
