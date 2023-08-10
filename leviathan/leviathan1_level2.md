Level #2 find the password for leviathan2 user

- Server: leviathan.labs.overthewire.org
- User: leviathan1
- Password: PPIfmI1qsA

ssh leviathan1@leviathan.labs.overthewire.org -p 2223

//once in the home dir look at the dir contents
ls -la

//the check file of type executable is in home dir
file check
./check

//executing ./check prompts for a password, tried the most common passwords and got leviathan2 user password

leviathan2 user password: mEh5PNl10e
