from random import randint

def draw_letters():
    weight_list = []
    letter_pool = { 
        "A": 9, "B": 2, "C": 2, "D": 4,
        "E": 12, "F": 2, "G": 3, "H": 2,
        "I": 9, "J": 1, "K": 1, "L": 4,
        "M": 2, "N": 6, "O": 8, "P": 2,
        "Q": 1, "R": 6, "S": 4, "T": 6,
        "U": 4, "V": 2, "W": 2, "X": 1,
        "Y": 2, "Z": 1
    } 
    for key, value in letter_pool.items():
        weight_list.extend([key] * value)

    count = 0
    draw_letter_list = []
    while count < 10: 
        random_number = randint(0, len(weight_list)-1)
        draw_letter_list.append(weight_list[random_number])
        weight_list.pop(random_number)
        count += 1

    return draw_letter_list

def uses_available_letters(word, letter_bank):
    rest_letter_bank = letter_bank.copy()
    word_list = []
    for letter in word.lower():
        word_list.append(letter)
        for i in range(len(rest_letter_bank)):
            if letter == rest_letter_bank[i].lower():
                rest_letter_bank.pop(i)
                word_list.remove(letter)
                break

    if word_list == []:
        #print("True")
        return True
    else:
        #print("False")
        return False

def score_word(word):
    letter_value = { 
            "A": 1, "B": 3, "C": 3, "D": 2,
            "E": 1, "F": 4, "G": 2, "H": 4,
            "I": 1, "J": 8, "K": 5, "L": 1,
            "M": 3, "N": 1, "O": 1, "P": 3,
            "Q": 10, "R": 1, "S": 1, "T": 1,
            "U": 1, "V": 4, "W": 4, "X": 8,
            "Y": 4, "Z": 10
        }
    
    value_sum = 0
    lower_letter_value = {}

    for key, value in letter_value.items():
        lower_letter_value[key.lower()] = value

    for letter in word.lower():
        value_sum += lower_letter_value[letter]

    if 6< len(word) < 11:
        value_sum += 8

    return value_sum

def get_highest_word_score(word_list):
    highest_score = 0
    highest_score_len = 0
    highest_score_word = ""
    for word in word_list:
        if score_word(word) > highest_score:
            highest_score = score_word(word)
            highest_score_len = len(word)
            highest_score_word = word
        elif score_word(word) == highest_score:
            if len(word) < highest_score_len:
                highest_score = score_word(word)
                highest_score_len = len(word)
                highest_score_word = word

        if len(word) >= 10:
            highest_score = score_word(word)
            highest_score_len = len(word)
            highest_score_word = word
            #print("test:", word)
            return (highest_score_word, highest_score)

    return (highest_score_word, highest_score)