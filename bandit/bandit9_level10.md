Level #10
- Server: bandit.labs.overthewire.org
- User: bandit9
- Password: EN632PlfYiZbn3PhVK3XOGSlNInNE00t

ssh bandit9@bandit.labs.overthewire.org -p 2220

#4 Print to stdout the contents of data.txt to get a grasp of the contents.
cat data.txt
#4 Grep the contents of data.txt using -a flag since it's a binary.
cat data.txt | grep -a "="
#4 Grep the contents of data.txt adding -E flag and {2,} to get only lines with more than one =.
cat data.txt | grep -a -E "={2,}"
User bandit10 password: G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
