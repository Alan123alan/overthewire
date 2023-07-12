Level #14 Read a file that can only be read by bandit14 user
- Server: bandit.labs.overthewire.org
- User: bandit13
- Password: wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

ssh bandit13@bandit.labs.overthewire.org -p 2220
The way I solved this level was by taking the ssh private key you get
access with user bandit13, then logged out server, created a private key file
in my local machine, changed permisions so that only my user could read/write private key
chmod 600 <file_name>
then added that file as the identity option in ssh command
ssh bandit14@bandit.labs.overthewire.org -p 2220 -i <file_name>
then once inside the server as user bandit14 I got access to file with bandit14 password
cat /etc/bandit_pass/bandit14
bandit14 user password: fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
