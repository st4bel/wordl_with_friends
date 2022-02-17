import os
import word_handler as wh



filename = "combined.txt"
static_path = os.path.join(os.path.dirname(__file__),"static")

words = wh.read_word_list(os.path.join(static_path, filename))

current_solve_word =  input("solve_word: ")
guesses = []
hints = []
while(True):

    guesses.append(input("Your {}. guess: ".format(len(guesses)+1)))
    guesses[-1] = guesses[-1].lower()
    if guesses[-1] not in words:
        if guesses[-1] == "exit":
            break
        print("Your guess '{}' is not valid.".format(guesses[-1]))
        guesses.pop(-1)
        continue
    hints.append(wh.get_hints(guesses[-1], current_solve_word))
    wh.draw_status(guesses, hints)
    

