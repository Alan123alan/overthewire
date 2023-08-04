#Level 26 logging in to bandit26 from bandit25. Be aware that bandit26 shell is not
/bin/bash, but something else. Find out what it is, how it works and how to break out

- Server: bandit.labs.overthewire.org
- User: bandit25
- Password: p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d 

ssh bandit25@bandit.labs.overthewire.org -p 2220

//once logged in as bandit25 you'll see a bandit26.sshkey
//use cat and copy it's contents
cat bandit26.sshkey
//create a new file in you local machine and copy the contents
vim bandit26.sshkey
//then connect to server

bandit26 user password: c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
