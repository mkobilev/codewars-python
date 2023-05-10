import string


def calc_score_for_word(word):
    alphabet = string.ascii_lowercase

    sum = 0
    for letter in word:
        if letter in alphabet:
            sum += alphabet.find(letter) + 1
        
    return sum

def high(text):

    word_list = text.split(' ')
    score = []
    
    for word in word_list:
        score.append(calc_score_for_word(word))
        
    return word_list[score.index(max(score))]