def unique_in_order(sequence):
    unique_sequence = []
    last_char = None
    for el in sequence:
        if el != last_char:
            unique_sequence.append(el)
        last_char = el
    return unique_sequence
