Level #18 Compare two files and find the different line to obtain bandit18 pwd
- Server: bandit.labs.overthewire.org
- User: bandit17
- Password: file bandit17_pk

//to log into server as bandit17 user use the identity file flag of ssh command
ssh bandit17@bandit.labs.overthewire.org -p 2220 -i bandit17_pk
//using diff command to check differences between two files
//adding -y flag to see output in two columns
//adding --suppress-common-lines flag to only output to stdout the line that 
//differs between the two files used as input
diff -y --suppress-common-lines passwords.old passwords.new
bandit18 user password: hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
