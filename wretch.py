#!/usr/bin/env python3

from matrix_client.client import MatrixClient
from matrix_client.api import MatrixHttpApi 

import json
import os

#Debugging tokens
config = open('config.ini', 'r')
config = config.read().splitlines()

matrixUsername = str(config[0])
matrixPassword = str(config[1])
matrixHost = str(config[2])
matrixTestRoom = str(config[3])

client = MatrixClient(matrixHost)
token = client.login_with_password(username=matrixUsername, password=matrixPassword)

room = client.join_room(matrixTestRoom)
room.send_text("Ahoy!")

#Load configuration file
def load_config(configFile):
    if not os.path.exists(configFile):
        print('No config')
    else:
        with open(configFile) as config:
            return json.load(config)

#Should the config contain API tokens?


def command(name, **options):
    '''Decorator for command functions.
    '''

    def decorator(f):
        options['method'] = f
        commands[name] = options
        return f
    return decorator

#def reload_commands():
    #unsure of how to reload commands.
#    '''Reload all source files in commands directory.'''
#    global commands
#    commands = dict()
#    #Globals dict for the command source. used to go here. This may just be handled from the MatrixClient

# room handling will be difficult. Do an event handler and handle room input individually.

def send(message):
    room.send_text(message)

def parse(data):
    ''' Parse a matrix message and return a tuple of its parts.
'''

def room_callback(room, incoming_event):
    print(incoming_event)

