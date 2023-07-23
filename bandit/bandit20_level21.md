Level #21 execute binary pass bandit20 password and receive bandit21 password

- Server: bandit.labs.overthewire.org
- User: bandit20
- Password: VxCazJaVykI6W36BkBU0mJTCM8rR95XT

ssh bandit20@bandit.labs.overthewire.org -p 2220
//the way to solve this problem needed me to better understand the problem

//first what the ./suconnect script does is to connect to a port in localhost
//the port is specified as an argument --> ./suconnect <port>
//after connecting, the script reads the stdout and checks if whatever is
//found matches bandit20 user password if so it returns bandit21 password
//but doing nmap is worth nothing since none of the open ports have
//bandit20 user password in the stdout
//solution to this includes starting a server at some random tcp supported port
nc -l -p 6127
//once server started, inputing bandit20 user password
//but then the current session will be halted by the spawn server at port 6127
//you will be stuck listening to incoming requests
//so previous to starting the server you can spawn 2 tmux windows one for server//and another for executing
./suconnect 6127
//after running script you'll see bandit21 password in server running at p 6127 

bandit21 user password: NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
