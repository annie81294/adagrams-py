from random import randint
LETTER_POOL = { 
        "A": 9, "B": 2, "C": 2, "D": 4,
        "E": 12, "F": 2, "G": 3, "H": 2,
        "I": 9, "J": 1, "K": 1, "L": 4,
        "M": 2, "N": 6, "O": 8, "P": 2,
        "Q": 1, "R": 6, "S": 4, "T": 6,
        "U": 4, "V": 2, "W": 2, "X": 1,
        "Y": 2, "Z": 1
    } 

LETTER_VALUE = { 
        "A": 1, "B": 3, "C": 3, "D": 2,
        "E": 1, "F": 4, "G": 2, "H": 4,
        "I": 1, "J": 8, "K": 5, "L": 1,
        "M": 3, "N": 1, "O": 1, "P": 3,
        "Q": 10, "R": 1, "S": 1, "T": 1,
        "U": 1, "V": 4, "W": 4, "X": 8,
        "Y": 4, "Z": 10
    }

HAND_SIZE = 10
LOW_MAGIC_NUMBER = 7
HIGH_MAGIC_NUMBER = 10

def draw_letters():

    weight_list = letter_pool_dic_to_list()

    draw_letter_list = []
    while len(draw_letter_list) < HAND_SIZE: 
        random_number = randint(0, len(weight_list)-1)
        draw_letter_list.append(weight_list[random_number])
        weight_list[random_number], weight_list[-1] = weight_list[-1], weight_list[random_number]
        weight_list.pop()

    return draw_letter_list

def letter_pool_dic_to_list():

    weight_list = []
    for key, value in LETTER_POOL.items():
        weight_list.extend([key] * value)

    return weight_list

def uses_available_letters(word, letter_bank):
    rest_letter_bank = letter_bank.copy()

    for letter in word.upper():
        if letter in rest_letter_bank:
            rest_letter_bank.remove(letter)
        else:
            return False
    
    return True


def score_word(word):
    value_sum = 0

    for letter in word.upper():
        value_sum += LETTER_VALUE[letter]

    if LOW_MAGIC_NUMBER <= len(word) <= HIGH_MAGIC_NUMBER:
        value_sum += 8

    return value_sum

def get_highest_word_score(word_list):
    highest_score = 0
    highest_score_len = 0
    highest_score_word = ""
    for word in word_list:
        #print("NOW:", word)
        current_score = score_word(word)
        if current_score > highest_score:
            highest_score = score_word(word)
            highest_score_len = len(word)
            highest_score_word = word
        elif current_score == highest_score:
            if len(highest_score_word) >= 10:
                #print("Loop1:", highest_score_word)
                break
            elif len(word) >= 10:
                highest_score = score_word(word)
                highest_score_len = len(word)
                highest_score_word = word
                #print("Loop2:", highest_score_word)
                break
            elif len(word) < highest_score_len:
                highest_score = score_word(word)
                highest_score_len = len(word)
                highest_score_word = word
                #print("Loop1:", highest_score_word)
          
    return (highest_score_word, highest_score)