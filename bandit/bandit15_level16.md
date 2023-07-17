Level #16 retrieve bandit16 password by submitting the bandit15 password to port 30001 on localhost using SSL encryption. 
- Server: bandit.labs.overthewire.org
- User: bandit15
- Password: jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

ssh bandit15@bandit.labs.overthewire.org -p 2220
openssl s_client 127.0.0.1:30001
//This will stablish encrypted SSL connection with server through port 30001
//Then you can submit bandit15 user password through stdin
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
//And you will get bandit16 user password as a response
Password for bandit16 user: JQttfApK4SeyHwDlI9SXGR50qclOAil1
