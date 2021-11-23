# Easy_Keesy

We have been provided a file named easy_keesy. After using the file command we see that it's a keepass file.

## Solution

After using the `keepass2john` function we get the hashfile of the file. We use

```
john --wordlist=rockyou.txt
```

to get the password for the keepass file.After opening it in keepass

```
keepass easy_keesy
```
we enter the password that we just got and we'll get the flag

```
flag{jtr_found_the_keys_to_kingdom}
```
This was a really nice an and interactive challenge.
