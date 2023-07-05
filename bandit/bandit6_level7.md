Level #7 find file with owned by user bandit6 and group bandit7 which size is 33 bytes and read it
- Server: bandit.labs.overthewire.org
- User: bandit6
- Password: P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

ssh bandit6@bandit.labs.overthewire.org -p 2220
find / -user bandit6 -group bandit7 -size 33c -exec grep -v "Permission denied" {} +
bandit7 user password: z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
