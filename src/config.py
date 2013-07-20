import os
import os.path
import time

# some commands can be executed only if the user's nick is found in this list
owner = list(set([
    'dougpiston',
]))

owner_email = {
    'asparks': 'asparks914@gmail.com',
}

# server to connect to
server = 'chat.freenode.net'
# server's port
port = 6667

# bot's nicknames
nicks = list(set(['Natalya']))
# bot's real name
real_name = 'Natalya'

# channels to join on startup
channels = list(set([
    '#xenapiadminproject',
]))

cmds = {
    # core commands list, these commands will be run in the same thread as the bot
    # and will have acces to the socket that the bot uses
    'core': list(set([
        'quit',
        'join',
        'channels',
    ])),

    # normal commands list, the ones that are accessible to any user
    'user': list(set([
        'wiki',
        'answer',
        'about',
        'help',
        'weather',
        'google',
        'mball',
        'uptime',
        'so',
        'website',
	'git' ,
    ])),

    # commands list that the bot will execute even if a human didn't request an
    # action
    'auto': list(set([
        'email_alert',
    ])),
}

# smtp server for email_alert
smtp_server = 'smtp.gmail.com'
smtp_port = 25
from_email_address = 'changeme@gmail.com'
from_email_password = 'p@s$w0rd'

# users should NOT modify below!
log = os.path.join(os.getcwd(), '..', 'logs', '')
start_time = time.time()
current_nick = ''
