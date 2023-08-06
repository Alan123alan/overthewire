Level #31 Clone repository at ssh://bandit30-git@localhost:/home/bandit30-git/repo via port 2220 and find password for the next level

- Server: bandit.labs.overthewire.org
- User: bandit30
- Password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

//password for bandit30-git user is the same as bandit30
ssh bandit30@bandit.labs.overthewire.org -p 2220

//once in server as bandit30 go /tmp folder where you have write permissions
git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo

//once the repo is cloned
cd repo
ls
cat README.md

//this time the README.md file has no information 
//first checked for branches, but only master existed
//checked git log but just the initial commit existed
//tried with a pull but repository was up to date
//tried to see if any tags and found a 'secret' tag
git branch -a
git log
git tag
> secret

//checked the contents of the git tag
git show secret

bandit31 user password: OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
