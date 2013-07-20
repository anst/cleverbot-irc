def website(components): # !website
    '''Returns a string containing info about the bot'''
    response = ''

    if components['arguments'] == '!website':
        # the user sent just the command, no garbage
        response = 'www.xenapiadmin.com'

    return response
