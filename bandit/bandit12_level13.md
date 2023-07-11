Level #13 Read hexdump file and find the password
- Server: bandit.labs.overthewire.org
- User: bandit12
- Password: JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

ssh bandit12@bandit.labs.overthewire.org -p 2220
This one was tricly for me, first th problem states that file is a hexdump from a file,
but the file was compressed multiple times using either gzip, bzip2 or tar, but this last
piece of information is not explained so to complete this level you needed to
reverse hexdump with: xxd -r data.txt
and after that do multiple iterations of using the file command to get details of the
type of compressed file you currently have then use the corresponding command for decompression
bandit13 user password: wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
