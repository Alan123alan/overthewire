Level #15 Submit bandit14 user password trough port 30000 to retrieve bandit15 user password
- Server: bandit.labs.overthewire.org
- User: bandit14
- Password: fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq

ssh bandit14@bandit.labs.overthewire.org -p 2220
once into the server as user bandit14 send password
through tcp (port 30000) using nc command
echo fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq | nc 127.0.0.1 30000
bandit15 user password: jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
