
Level #9 find th unique string in file
- Server: bandit.labs.overthewire.org
- User: bandit8
- Password: TESKZC0XvTetK0S9xNwm25STk5iWrBvP

//secure shell connection as bandit8 user
ssh bandit8@bandit.labs.overthewire.org -p 2220
//according to man page uniq command works for report or filtering repeated strings
//tried to use the uniq command with the -u (keep only unique strings) on cat data.txt output but didn't work
//seems that it needs to be sorted in order for the uniq command to work
sort data.txt | uniq -u
Password for user bandit9: EN632PlfYiZbn3PhVK3XOGSlNInNE00t
