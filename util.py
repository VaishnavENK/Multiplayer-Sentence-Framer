def has_forbidden_chars(forbidden_chars, string):
    for char in string:
        if char in forbidden_chars:
            return True
    return False