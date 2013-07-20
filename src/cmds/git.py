def git(components): # !git
    '''Returns our github page'''
    response = ''

    if components['arguments'] == '!git':
        # the user sent just the command, no garbage
        response = 'https://github.com/Xenapi-Admin-Project/xe-manpages'

    return response
