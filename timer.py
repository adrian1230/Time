import time

hour = int(input('how many hour: '))
minute = int(input('how many minute: '))
second = int(input('how many second: '))
start, a, b, c = 0, 0, 0, 0
end = hour * 60 * 60 + minute * 60 + second

print('{} hour {} minute {} second\n'.format(a,b,c))

while start < end:
    c += 1
    start += 1
    print('{} hour {} minute {} second\n'.format(
        a,b,c
        ))
    print(start,a,b,c)
    time.sleep(1)
    if c == 60:
        c = 0
        b += 1
    if b == 60:
        b = 0
        a += 1
        






