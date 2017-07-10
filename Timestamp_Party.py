# -*- coding: utf-8 -*-
# author: pBouillon - https://github.com/pBouillon

import time
from time import sleep
from time import time

def beep():
    print ('\a')

if __name__ == '__main__':
    awaited_timestamp = 1500000000
    ctsp = 0
    waiting = True

    while (waiting) :
        ctsp = int(time())
        if ctsp == awaited_timestamp :
            waiting = False
        sleep(.3)

    beep ()
    print ("""\n
    ************************\n
         Merry Timestamp !  \n
            1500000000      \n
    ************************"
    \n""")
    beep ()
