from time import sleep
from random import randint
while True:
    sleep(.05)
    data = ''
    with open('board.txt', 'r') as board:
        data = board.read()

    if data.split('\n')[0] == 'b':
        with open('board.txt', 'w') as board:
            board.write(str(randint(0,7))+str(randint(0,7))+str(randint(0,7))+str(randint(0,7))+'\n'+data.split('\n')[1])