Level #32 Clone repository at ssh://bandit31-git@localhost:/home/bandit31-git/repo via port 2220 and find password for the next level

- Server: bandit.labs.overthewire.org
- User: bandit31
- Password: OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt

//password for bandit31-git user is the same as bandit31
ssh bandit31@bandit.labs.overthewire.org -p 2220

//once in server as bandit31 go /tmp folder where you have write permissions
git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo

//once the repo is cloned
cd repo
ls
cat README.md

//this time the README.md file ask to create a key.txt file
//edit the file the text 'May I come in?'
//add the file to stage
//commit the changes and push to remote
//one issue is that there is a .gitignore file with *.txt pattern to work around this
git add -f key.txt
git commit -m "Added file"
git push origin main
 
//once push is completed and accepted you will be prompted with next level password

bandit32 user password: rmCBvG56y58BXzv98yZGdO7ATVL5dW8y
