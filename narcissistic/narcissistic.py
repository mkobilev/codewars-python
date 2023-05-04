def narcissistic( value ):
    value_str = str(value)
    multiplicator = len(value_str)
    
    if multiplicator < 2:
        return True

    digit_list = [int(x) for x in value_str]
    sum = 0
    for digit in digit_list:
        sum += digit**multiplicator
    return sum == value
