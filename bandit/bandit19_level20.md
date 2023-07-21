Level #20 use setuid binary then get bandit20 password from /etc/bandit/pass

- Server: bandit.labs.overthewire.org
- User: bandit19
- Password: awhqfNnAbc1naukrpqDYcF95h7HoMTrC

ssh bandit19@bandit.labs.overthewire.org -p 2220
//after running bandit20-do executable without arguments
//you get "execute a command as someone else"
//since all bandits user passwords are located at /etc/bandit_pass
//but only you can read current user file with password
//we use the bandit20-do executable tu run cat /etc/bandit_pass/bandit20
./bandit20-do cat /etc/bandit_pass/bandit20
//and we get
bandit20 user password: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
