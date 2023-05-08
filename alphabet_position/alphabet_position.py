import string

def alphabet_position(text):
    text = text.lower()
    result = []
    alphabet = string.ascii_lowercase
    for char in text:
        if char in alphabet:
            result.append(str(alphabet.find(char) + 1))
            
    return ' '.join(result)
