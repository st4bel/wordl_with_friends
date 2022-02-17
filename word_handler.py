import os
chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def read_word_list(filepath):
    f = open(filepath, 'r')
    words = f.readlines()
    for i in range(len(words)):
        words[i] = words[i].strip()
    return words

def get_hints(guess, solve_word):
    f = [-1] * len(solve_word)
    hints = {} # char_pos of guess : [char_pos of solve]
    for i in range(len(guess)):
        positions = [pos for pos, char in enumerate(solve_word) if char == guess[i]]
        if guess[i] not in hints:
            hints[guess[i]] = positions
        if i in positions: # char of guess in right position
            f[i] = 1
            hints[guess[i]].remove(i)
    for i in [j for j in range(len(f)) if f[j] != 1]: # for every position in guess, which char is not in right position
        if hints[guess[i]] != []:
            f[i] = 0
            hints[guess[i]].pop(0)

    return f

def update_not_allowed(guess, hints, not_allowed, required_chars):
    for i in range(len(hints)):
        c = guess[i]
        if hints[i] == 1: 
            not_allowed[i] = [char for char in chars if char != c]
        elif hints[i] == 0:
            if i not in not_allowed:
                not_allowed[i] = [c]
            elif c not in not_allowed[i]:
                not_allowed[i].append(c)

    current_req = {}
    for i in range(len(hints)):
        c = guess[i]
        if hints[i] != -1:
            if c not in current_req:
                current_req[c] = 0
            current_req[c] += 1
             

    return not_allowed, required_chars

def update_restrictions(guess, hints, restrictions = {}):
    if restrictions == {}:
        restrictions = init_restrictions(len(guess))
    for i in range(len(hints)):
        if restrictions[i]["char_is"]:
            continue
        if hints[i] == 1:
            restrictions[i]["char_is"] = guess[i]
        elif hints[i] == 0:
            if guess[i] in restrictions[i]["char_allowed"]:
                restrictions[i]["char_allowed"].remove(guess[i])
        else:
            for j in range(len(hints)):
                if guess[i] in restrictions[j]["char_allowed"]:
                    restrictions[j]["char_allowed"].remove(guess[i])
    return restrictions


def init_restrictions(length):
    restrictions = {}
    for i in range(length):
        restrictions[i] = {"char_is" : False, "char_allowed" : [char for char in chars]}
    return restrictions


def draw_status(guesses, hints):
    colors = {-1:"_", 0:":", 1:"1"}
    os.system("cls")
    print("current status:")
    for i in range(len(guesses)):
        print(guesses[i])
        for j in range(len(hints[i])):
            print(colors[hints[i][j]], end="")
        print("")
    
def check_solve_word(solve_word, restrictions):
    result = True
    for i in range(len(solve_word)):
        if restrictions[i]["char_is"]:
            if solve_word[i] != restrictions[i]["char_is"]:
                print("Char #{} must be '{}'!".format(i+1, restrictions[i]["char_is"]))
                result = False
        elif solve_word[i] not in restrictions[i]["char_allowed"]:
            print("Char #{} can't be '{}'!".format(i+1, solve_word[i]))
            result = False
    return result



