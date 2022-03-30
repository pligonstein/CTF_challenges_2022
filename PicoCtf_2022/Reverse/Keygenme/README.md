Can you get the flag?

Reverse engineer this [binary](https://artifacts.picoctf.net/c/519/keygenme).

After downloading the file we run the `file` command to see what we're up against.

`keygenme: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=98b36efa79e3771a1c70e96e1b0a4db0cde2f28e, for GNU/Linux 3.2.0, stripped
`

We decided to open it in ghidra and see what we have in the main function.Going through it we find the first part of the flag.

  `buffer._0_8_ = 0x7b4654436f636970;`
  
  `buffer._8_8_ = 0x30795f676e317262;`
  
  `buffer._16_8_ = 0x6b5f6e77305f7275;`
  
  `buffer._24_4_ = 0x5f7933;`
  
  `picoCTF{br1ng_y0ur_0wn_k3y_`
  
  After analysing a little bit more we see that we need to do `md5sum` on each part of the flag: `picoCTF{br1ng_y0ur_0wn_k3y_` 
  as well as the suffix `}` and then concatenate  them so we can get the last part of the flag.
  
  `  MD5((uchar *)buffer,len_buf,md5_buf);`
  
  `len_buf = strlen((char *)&suffix);`
  
  `MD5((uchar *)&suffix,len_buf,md5_suffix);`
  
  `offset = 0;`
 
 `for (i = 0; i < 16; i = i + 1) {`
    `sprintf(buffer + (long)offset + 32,"%02x",(ulong)md5_buf[i]);`
    `offset = offset + 2;`
  
  `}`
  
  `offset = 0;`
  
  `for (j = 0; j < 16; j = j + 1) {`
    `sprintf(buffer + (long)offset + 64,"%02x",(ulong)md5_suffix[j]);`
    `offset = offset + 2;`
  
  `}`
  
  `  flag[27] = buffer[58];`
  
  
  `flag[28] = buffer[46];`
  
  `flag[30] = buffer[57];`
  
  `flag[31] = buffer[61];`
  
  `flag[32] = buffer[44];`
  
  `flag[33] = buffer[57];`
  
  `flag[34] = buffer[44];`
  
  `flag[35] = (undefined)suffix;`
  
  To calculate the md5 value of the string just run those command:
  
  ```
  echo -n "picoCTF{br1ng_y0ur_0wn_k3y_" | md5sum 
  ```
  ```
  echo -n "}" | md5sum
  ```
  After getting the value for each I just concatenated them in a variable named `str`
  
  `str = "cbb184dd8e05c9709e5dcaedaa0495cf438218d572e90162d0981cbbc7d43882"`
  
  And then I did it by hand by calculating each letter/number mentioned previous in `flag[]=buffer[]` and we get the flag
  
  `picoCTF{br1ng_y0ur_0wn_k3y_d6f78070}`
