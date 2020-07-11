def check_email(string):
    if ' ' in string:
        return False
    if '@' not in string:
        return False
    if string.find('.', string.find('@') + 2) == - 1:
        return False
    return True
