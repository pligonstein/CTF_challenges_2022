Can you get the flag?

Download this [binary](https://artifacts.picoctf.net/c/121/gdbme).

Here's the test drive instructions:

```
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```
This was an easy challenge as we only had to download the file and open it in gdb, followed by the previous commands.

`
picoCTF{d3bugg3r_dr1v3_7e8f2155}
`
