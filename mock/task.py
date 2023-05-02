def to_camel_case(text):
    dividers = ['-', '_']
    camel_case = ''
    flag = False
    for indx, char in enumerate(text):

        if flag == True:
            camel_case += text[indx].capitalize()
            flag = False
            continue

        if char in dividers:
            flag = True
            continue

        camel_case += text[indx]
    return camel_case



import re

def to_camel_case(text):
    return re.sub(r'[-_](\w)', lambda m: m.group(1).upper(), text)