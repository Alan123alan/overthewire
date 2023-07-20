Level #19 Password is in readme file but .bashrc file is modified to log you out after succesful ssh connection

- Server: bandit.labs.overthewire.org
- User: bandit18
- Password: hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

//since everytime you try to stablish a SSH connection a terminal is load
//and ‘.bashrc’ file is run every time a terminal is loaded you get logged out
//the workaround to this unconveinance is to directly execute the cat command
//through the stablished ssh connection
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
//this is possible since problem states that password is in readme file inside
//home directory
bandit19 user password: awhqfNnAbc1naukrpqDYcF95h7HoMTrC
