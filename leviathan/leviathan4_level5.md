Level #5 find the password for leviathan5 user

- Server: leviathan.labs.overthewire.org
- User: leviathan4
- Password: AgvropI4OA

ssh leviathan4@leviathan.labs.overthewire.org -p 2223

//once in the home dir look at the dir contents
ls -la

// a suspicious dir is the .trash dir
cd .trash
ls -la

// inside this dir bin executable file can be found
./bin

// this executable outputs a series of 8 bit binary digits that I inmmediatly supposed was the password for leviathan5
// there are multiple ways of solving this but since I'm practicing C programming I decided to write the following C program

#include <stdio.h>
#include <string.h>
#include <math.h>

double binary_to_dec(char binary[], int numer_of_bits);


double binary_to_dec(char binary[], int number_of_bits)
{
        double dec = 0;
        for(int i = 0; i < number_of_bits; i++){
                char bit = binary[i];
                if(bit == '1'){
                        dec += pow(2, (7 - i));
                }
        }
        return dec;
}

int main(int argc, char *argv[])
{
        for(int i = 1; i < argc; i++){
                int arg_len = strlen(argv[i]);
                int dec = binary_to_dec(argv[i], arg_len);
                printf("%c", dec);
        }
        return 0;
}

leviathan5 user password: EKKlTF1Xqs
