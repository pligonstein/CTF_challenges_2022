This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.

You can download the file from [here](https://artifacts.picoctf.net/c/329/Flag.pdf).

For this challenge you're provided with a `Flag.pdf`. Running 

```
file Flag.pdf
```

On the current file that we got we see that it is actually `Flag.shar: shell archive text` and not a pdf, which is a file type that can
nest other file types in it. After renaming it to `Flag.shar` we can unshar it with this command:

```
unshar Flag.shar
```
After decompressing it we get another `flag` file that we need to look for the its file type:

```
file flag
```
And we see that this time we got a `ar archive` that we got to decompress. After renaming the current file to our need we can decompress it

```
mv flag flag.a
```

Fortunately, there already is a command line tool that we can use to decompress the file:

```
ar -x flag
```

After decompressing we are provided with another file to decompress. We need to repeat the same previous process for a couple of times
by using different command line tools to decompress them. When you're done you're only gonna have a `ASCII text` flag file that you need
to convert its content from hex to string and you'll get the flag.

`picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_278f1a18}`

