Level #1 get password for leviathan1

- Server: leviathan.labs.overthewire.org
- User: leviathan0
- Password: leviathan0

ssh leviathan0@leviathan.labs.overthewire.org -p 2223

//once in home dir start by exploring the folder structure
ls -la
//the .backup dir has explicit permissions only for user leviathan0
cd .backup
//inside the .backup dir there is only the bookmarks.html file
cat bookmarks.html
//since it has a lot of lines grep the file for a desired pattern
cat bookmarks.html | grep password

leviathan1 user password: PPIfmI1qsA
