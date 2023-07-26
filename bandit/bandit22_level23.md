Level #23 Look in etc/cron.d/ for the configuration and see what command is being executed

- Server: bandit.labs.overthewire.org
- User: bandit23
- Password: WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff


ssh bandit22@bandit.labs.overthewire.org -p 2220
//went into /etc/cron.d and read file cronjob_bandit23
//this cronjob executes as user bandit23 the file at /usr/bin/cronjob_bandit.sh
//read file /usr/bin/cronjob_bandit.sh and it is a script which executes the whoami command
//the output of the whoami cmd is stored in variable ($myname), the concatenated to a string, piped to md5sum, piped to a cut command
//the output of this is saved in another variable ($mytarget) the used as the output path to bandit23 user password 
//cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit23 user password: QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G
