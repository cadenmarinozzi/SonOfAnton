"""
staticQuery takes a query such as "What time is it?", splits it into tokens, finds keword tokens such as argument tokens-
and command tokens and then finds the command being queried
"""

from query.commands import commands

def tokenize(string):
    return string.split(' ');

def parse(tokens): # This doesn't need to be fast. Just accurate.
    parsed = {
        'args': []
    };
 
    #                                               |
    #                                               v
    for token in tokens: # Find the command "what time is it"
        if (token in commands):
            command = commands[token];
            parsed['command'] = command;
            parsed['commandName'] = token;

            break; # The command could come after the args, type, etc

    if ('command' in parsed):
        #                                                   |
        #                                                   v
        for token in tokens: # Find the args "what time is it"
            if ('args' in parsed['command']):
                if (token in parsed['command']['args']):
                    parsed['args'].append(token);

                continue;

            if (token != parsed['commandName']):
                parsed['args'].append(token);

        return parsed;

def staticQuery(query):
    tokens = tokenize(query);

    if (len(tokens) > 1): # Full query "what time is it"
        parsed = parse(tokens);

        if (parsed):
            callback = parsed['command']['callback'];
            
            if ('args' in parsed):
                callback(parsed['args']);
            else:
                callback();

            return True; # Success
    else: # Single word query "time"        
        if (query in commands):
            command = commands[query];
            command['callback']();

        return True; # Success