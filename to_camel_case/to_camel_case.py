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



def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')