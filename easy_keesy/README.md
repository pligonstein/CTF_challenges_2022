# Easy_Keesy

We have been provided a file named easy_keesy. After using the file command we see that it's a keepass file.

## Solution

After using the `keepass2john` function we get the hashfile of the file. We use

```
john --wordlist=rockyou.txt
```

to get the password for the keepass file.
