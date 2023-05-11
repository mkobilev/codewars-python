def rgb(r, g, b):
    result_string = ''
    for el in (r, g, b):
        if el <= 0:
            result_string += '00'
        elif el > 255:
            result_string += 'FF'
        else:
            result_string += hex(el)[2:].zfill(2)

    return result_string.upper()
