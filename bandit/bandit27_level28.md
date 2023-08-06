Level #28 clone a git repository at ssh://bandit-27@localhost/home/bandit-27/repo via the port 2220 pwd for bandit27-git = bandit27

- Server: bandit.labs.overthewire.org
- User: bandit27
- Password: 

//first step was to connect to server as bandit27 user
ssh bandit27@bandit.labs.overthewire.org -p 2220

//once connected to the server create a folder to clone the git repository
//an available folder to create files is the /tmp folder
mkdir /tmp/bandit27-git-repo
cd /tmp/bandit27-git-repo

//once folder is created and you are in the folder, you can
git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo

//once clone is complete
cd repo
cat README

bandit28 user password: AVanL161y9rsbcJIsFHuw35rjaOM19nR
