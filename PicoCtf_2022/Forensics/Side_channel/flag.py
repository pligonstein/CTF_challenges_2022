import time
import os

pin = ''
mx = 0
digit = 0

while len(pin) != 8:
    mx = 0
    for i in range (0,10):
        start = time.time()
    #print(start)
        num = pin + str(i)
        num = num.ljust(8,'0')
        print('[+]Code :' + num,end='\r')
        os.system("bash -c 'echo {} | ./pin_checker >/dev/null 2>&1'".format(num))
        end = time.time()
        dif = end-start
        #print(dif)
        if(dif > mx):
            mx = dif
            digit = str(i)
    pin = pin + digit

os.system("bash -c 'echo {} | ./pin_checker >/dev/null 2>&1'".format(pin))
print('[+] Code found :' + pin)
		
