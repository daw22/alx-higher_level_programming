#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        subs = 0
    else:
        subs = 32
    print('{}'.format(chr(i - subs)), end='')
