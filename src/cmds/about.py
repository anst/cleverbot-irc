def about(components): # !about
    '''Returns a string containing info about the bot'''
    response = ''

    if components['arguments'] == '!about':
        # the user sent just the command, no garbage
        response = 'andy___ is my owner'

    return response
