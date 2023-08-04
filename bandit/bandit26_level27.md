Level #27 Once you get a shell for bandit26 grab the password for bandit27

- Server: bandit.labs.overthewire.org
- User: bandit26
- Password: bandit26.sshkey

//performed the same actions to get the shell for bandi26
ssh bandit26@bandit.labs.overthewire.org -p 2220 -i bandit26.sshkey
//before executing the ssh command make the terminal as small as possible
//the terminal being smaller that the text that the more command will enter a scroll mode
//more commad description: used to view the text files in the command prompt, displaying one screen at a time in case the file is large (For example log files). The more command also allows the user do scroll up and down through the page.
//once more command enters scroll mode you can enter "v" and it will open the currently displayed file
//in vim, once in vim you can :set shell=/bin/bash then spawn the shell with :shell
//once in bandit26 shell
ls
file bandit27-do  
//it's and ELF so execute it
./bandit27-do
//you will be prompted with a message letting you know that it executes commands given as user bandi27
//so ask for bandit27 password
./bandit27-do cat /etc/bandit_pass/bandit27



bandit27 user password: YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
