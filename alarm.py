import time
import os

print('this alarm runs on your localtime\n')

snooze = int(input('how many snooze >>> '))

print('')

print('the current time is:\n{}\n'.format(
    time.ctime()
))

print('hour from 0 - 23, minute from 0 - 59\n')

dh = int(input('enter the hour here: '))
print('')
dm = int(input('enter the minute here: '))
print('')

if dh >= 24 or dh < 0:
    raise ValueError('you do not understand time')

if dm >= 60 or dm < 0:
    raise ValueError('you do not udnerstand time')

hour = 0

minute = 0

ah = time.localtime().tm_hour

am = time.localtime().tm_min

sec = time.localtime().tm_sec

if dh < ah:
    hour = 24 - ah + dh 
    hour = hour * 60 * 60

elif dh == ah:
    pass

else:
    hour = dh - ah
    hour = hour * 60 * 60

if dm < am:
    minute = 60 - am + dm 
    minute = minute * 60

elif dm == am:
    pass

else:
    minute = dm - am
    minute = minute * 60

c = 0

while c < (hour + minute - sec):
    print(c)
    time.sleep(1)
    c += 1

for i in range(snooze + 1):
    os.system('afplay l.mp3')
