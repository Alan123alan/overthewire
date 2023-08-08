Level #33 escape the upper shell madness

- Server: bandit.labs.overthewire.org
- User: bandit32
- Password: rmCBvG56y58BXzv98yZGdO7ATVL5dW8y

ssh bandit32@bandit.labs.overthewire.org -p 2220

//once in the server you are automatically sent to the uppershell
//after playing around with it for a bit I realized ENV variables and simbols could be used
//everything else got uppercased and didn't work
//searched for a way to exit a shell without using letters and this came up
$0
//after using it you get into a normal bash shell as user bandit33
//so I used bandit33 privileges to look into
cat /etc/bandit_pass/bandit33

bandit33 user password: odHo63fHiFqcWWJG9rLiLDtPm45KzUKy
