Level #4 find the password for leviathan4 user

- Server: leviathan.labs.overthewire.org
- User: leviathan3
- Password: Q0G8j4sakn

ssh leviathan3@leviathan.labs.overthewire.org -p 2223

//once in the home dir look at the dir contents
ls -la

//there is one executable file so try execute it
./level3

//it prompts for a password
//run the strings command on it to check if password is hardcoded in an obvious way
strings level3

//got lots of strings as output so let's check function calls with ltrace
ltrace ./level3

//there is a couple of strcmp function calls one seems to compare two hardcoded strings
//but in the second call for strcmp we see the password we entered compared against "snlsprintf\n"
//so on next run enter "snlsprintf" as password and hit enter

leviathan4 user password: AgvropI4OA
