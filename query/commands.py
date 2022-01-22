"""
This file contains the static commands that can be run
"""

commands = {};

import IO.io as io, json, random
from datetime import datetime

with open('query/phrases.json') as phrasesFile:
    phrases = json.loads(phrasesFile.read());

def fillResponse(command, response): # Fill a response with words relating to it. "10:50 AM" -> "It is 10:50 AM"
    commandFiller = phrases['filler'][command];
    filler = commandFiller[random.randint(0, len(commandFiller) - 1)];

    return f'{filler} {response}';

def time(args=None):
    curTime = datetime.now();
    time = curTime.strftime('%H:%M %p');

    if (args):
        if (
            'seconds' in args and 
            (
                'with' in args or
                'using' in args or
                'including' in args or 
                'includes' in args
            )
        ):
            time = curTime.strftime('%H:%M:%S %p');
    
    io.out(fillResponse('time', time));

commands['time'] = {
    'callback': time
};