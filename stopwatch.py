import time

a,b,c=0,0,0

while True:
    print('{} hr {} min {} sec'.format(
        a,b,c
    ))
    time.sleep(1)
    c += 1
    if c == 60:
        c = 0
        b += 1
    if b == 60:
        b = 0
        a+= 1
