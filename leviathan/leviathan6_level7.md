Level #7 find the password for leviathan7 user

- Server: leviathan.labs.overthewire.org
- User: leviathan6
- Password: YZ55XPVk2l 

ssh leviathan6@leviathan.labs.overthewire.org -p 2223

// once in the home dir look at the dir contents
ls -la

// this shows there is a leviathan6 executable file
./leviathan6

// after executing the leviathan6 file you get info about it's usage
// seems like you need to input a 4 digit code, already assuming leviathan7 password is the output once code is cracked
// brute forced this with a bash script
for i in seq(0000 9999)
do
	result=~/leviathan6 $i
	if [ $result != 'Wrong' ]
	then
		echo $i
		echo $result
	fi
done

// this bash script was created at /tmp/brute
// with force.sh as name
mkdir /tmp/brute
cd /tmp/brute
touch force.sh

// bash script kinda did its work it stoped looping after printing 7923
// this was because after the correct digit code is provided as input to leviathan6 executable
// a new shell as user leviathan7 is started that's why the bash script stops
./leviathan 7923
cat /etc/leviathan_pass/leviathan7

leviathan7 user password: 8GpZ5f8Hze
