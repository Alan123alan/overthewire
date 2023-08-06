Level #30 Clone repository at ssh://bandit29-git@localhost:/home/bandit29-git/repo via port 2220 and find password for the next level

- Server: bandit.labs.overthewire.org
- User: bandit29
- Password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

//password for bandit29-git user is the same as bandit29
ssh bandit29@bandit.labs.overthewire.org -p 2220

//once in server as bandit29 go /tmp folder where you have write permissions
git clone ssh://bandit29-git@localhost:2220/home/bandit28-git/repo

//once the repo is cloned
cd repo
ls
cat README.md

//the problem is that the README.md file has a note "no passwords in production"
//the first thing that came to mind was that password was in a branch reserved for development
git branch
>* master

//but running
git branch -a
//returned that master is set in production branch so moving it to dev branch will probably help

git checkout <path of dev branch>
ls
cat README.md

bandit30 user password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS
