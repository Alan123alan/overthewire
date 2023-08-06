Level #29 Clone repository at ssh://bandit28-git@localhost:/home/bandit28-git/repo via port 2220 and find password for the next level

- Server: bandit.labs.overthewire.org
- User: bandit28
- Password: AVanL161y9rsbcJIsFHuw35rjaOM19nR

//password for bandit28-git user is the same as bandit28
ssh bandit28@bandit.labs.overthewire.org -p 2220

//once in server as bandit28 go /tmp folder where you have write permissions
cd /tmp
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo

//once the repo is cloned
cd repo
ls
cat README.md

//the problem is that the README.md file has a placeholder ********** instead of the password
//the first thing that came to mind was that complete password was in another branch
git branch
>* master

//once confirmed only master branch exists second option was a previous commit
git log

//current commit had a message like "fixed data leak" so went back to the previous commit
git checkout <previous commit id>
ls
cat README.md

bandit29 user password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S
