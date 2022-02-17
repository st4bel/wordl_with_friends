import os
import word_handler as wh



filename = "combined.txt"
static_path = os.path.join(os.path.dirname(__file__),"static")

words = wh.read_word_list(os.path.join(static_path, filename))

#current_solve_word =  input("solve_word: ")
guesses = []
hints = []
not_allowed = {}
required_chars = []
restrictions = wh.init_restrictions(5)
while(True):
    guesses.append(input("Your {}. guess: ".format(len(guesses)+1)))
    guesses[-1] = guesses[-1].lower()
    if guesses[-1] not in words:
        if guesses[-1] == "exit":
            break
        print("Your guess '{}' is not valid.".format(guesses[-1]))
        guesses.pop(-1)
        continue
    while(True):
        solve_word = input("Enter the solution: ")
        if solve_word not in words:
            print("Your solution '{}' is not valid.".format(solve_word))
            continue
        if wh.check_solve_word(solve_word, restrictions):
            break

    hints.append(wh.get_hints(guesses[-1], solve_word))
    wh.draw_status(guesses, hints)
    restrictions = wh.update_restrictions(guesses[-1], hints[-1], restrictions)
    #for i in range(len(restrictions)):
    #    print(restrictions[i])


    

