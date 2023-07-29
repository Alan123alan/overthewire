Level #24 Check command being executed by cron then write a bash script to retrieve bandit24 password

- Server: bandit.labs.overthewire.org
- User: bandit23
- Password: QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G

ssh bandit23@bandit.labs.overthewire.org -p 2220
//the cronjob being executed was at /etc/cron.d/cronjob_bandit24
//this cronjob executed every minute the bash script at /usr/bin/cronjob_bandit24.sh
//the main takeaway from bash script is that it looked into /var/spool/bandit24/foo folder
//and it executed any script that it encountered with bandit24 user permissions
//taking advantage of the bandit24 permissions we copied it's password file from /etc/bandit_pass/bandit24
//into /tmp/bandit24/pass

//script for password copy
!#/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/bandit24/pass


//the previous script was copied from /tmp/bandit/script.sh into /var/spool/bandit24/foo/script.sh
//and executed by the cron


//as a prerequisite it was needed to change /tmp/bandit24 folder permissions so that anyone could wrx
chmod 777 -R /tmp/bandit24


bandit24 user password: VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar
