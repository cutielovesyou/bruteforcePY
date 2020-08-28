import random
from colored import fg, attr
a=0
def ah(length):
    return random.randint(10**(length-1),(10**length)-1)
while True:
    while True:
        try:
            b=int(input('Enter length:\n'))
            break
        except ValueError:print('\nEnter a number.\n')
        else:print(f'\n{ah(b)}\n')
    e=random.randint(10**(b-1),(10**b)-1)
    while True:
        a=a+1
        d=random.randint(10**(b-1),(10**b)-1)
        if d==e:
            print(f'{a} - {fg(2)}{d}{attr(0)}')
            break
        print(f'{a} - {fg(1)}{d}{attr(0)}')
