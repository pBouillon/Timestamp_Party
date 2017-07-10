# -*- coding: utf-8 -*-
# author: pBouillon - https://github.com/pBouillon

import telegram.ext
from telegram.ext   import Updater
from telegram.ext   import CommandHandler
from telegram.ext   import MessageHandler

import time
from time           import sleep


''' constant : str = bot's token '''
TOKEN = 'your_token_goes_here'


def alert (bot, update):
    '''Send an alert

    Warn the user the bot is running
    Send a notification on the awaited Timestamp
    '''
    update.message.reply_text (
        'Aknowledged {}, I\'ll alert you\n'\
        'Meanwhile, I won\'t be able to perform another action '\
        '(looks like I need a patch)'
        .format(update.message.from_user.first_name)
    )
    wait4it ()
    update.message.reply_text (
        'Merry Timestamp !\nIt reached 1 500 000 000 !'
    )

def cmd_list (bot, update) :
    msg = 'My commands:                               \n'\
          '/alert_me    -> start the countdown        \n'\
          '/progress    -> display the current timestamp'
    update.message.reply_text (msg)

def display_ctd (bot, update):
    msg = 'The current Timestamp is '
    msg += str(int(time.time()))
    print(msg)
    update.message.reply_text (msg)

def start (bot, update):
    update.message.reply_text (
        'Greetings!\nSend me /list to see what I\'m capable of !'
    )

def wait4it ():
    '''Wait until the awaited timestamp

    Wait until timestamp reached 1500000000
    Then return
    '''
    ctsp = 0
    while (True) :
        ctsp = int (time.time())
        if ctsp == 1500000000 :
            return
        sleep(.3)


if __name__ == '__main__':
    updater = Updater (TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start',    start))
    updater.dispatcher.add_handler(CommandHandler('list' ,    cmd_list))
    updater.dispatcher.add_handler(CommandHandler('progress', display_ctd))
    updater.dispatcher.add_handler(CommandHandler('alert_me', alert))

    updater.start_polling()
    updater.idle()
