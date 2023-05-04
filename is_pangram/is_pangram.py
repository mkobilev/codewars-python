import string

def is_pangram(s):
    ascii_lowercase = string.ascii_lowercase
    found_chars = []

    for char in s.lower():
        if char in ascii_lowercase and char not in found_chars:
            found_chars.append(char)

    return len(ascii_lowercase) == len(found_chars)


# Better solution / early return

import string


def is_pangram(s):
    s = s.lower()
    for char in string.ascii_lowercase:
        if char not in s:
            return False
    return True