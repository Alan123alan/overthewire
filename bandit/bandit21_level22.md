Level #22 Figure out which command is being executed at regular intervals

- Server: bandit.labs.overthewire.org
- User: bandit21
- Password: NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

ssh bandit21@bandit.labs.overthewire.org -p 2220
//the problem tells us to check /etc/cron.d/ to check what is being executed
cd /etc/cron.d
//inside this folder you will find some crontabs but since this is for
//finding bandit22 password I read the cronjob_bandit22
cat cronjob_bandit22 
//which seem to execute a bash script at /etc/bin/cronjob_bandit22.sh
vim /usr/bin/cronjob_bandit22.sh
//while inspecting the shell script I could see that it changes permissions of a file
//and then it writes the file whith the contents of the file /etc/bandit_pass/bandit22
//to the file /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
//so to get the password I went and read this file
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv


bandit22 user password: WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff
