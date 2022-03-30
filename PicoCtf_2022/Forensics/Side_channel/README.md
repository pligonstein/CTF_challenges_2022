There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?

Download the PIN checker program here [pin_checker](https://artifacts.picoctf.net/c/149/pin_checker)

Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master 
server using `nc saturn.picoctf.net 53932` and provide it the PIN to get your flag.

To solve this challenge we can either do `timing-based side-channel attacks` or do a brute force script to get 
each digit of the pin. I went with the second choice and so it was very easy to get the flag.

`picoCTF{t1m1ng_4tt4ck_18704dda}`
