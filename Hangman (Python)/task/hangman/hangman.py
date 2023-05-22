# Write your code here
import random

wordings = "Hangman"
answer_list = ["python", "java", "swift", "javascript"]
attempt = 8
win = 0
lose = 0
user_input_set = []
is_ended = False


def convert_list(wordings):
    return list(wordings)


def print_title():
    print(' '.join(wordings.upper()))


def user_input():
    # global user_input_set
    global attempt
    userInput = input("Input a letter: > ")
    if len(userInput) != 1:
        print("Please, input a single letter.")
    elif not userInput.islower():
        print("Please, enter a lowercase letter from the English alphabet.")
    elif userInput in user_input_set:
        print("You've already guessed this letter.")
        # attempt -= 1
    else:
        user_input_set.append(userInput)
        check_answer(userInput)


def check_answer(char):
    global masked_answer, attempt
    global is_ended
    global win
    if char in answer:
        index = (answer.index(char))
        masked_answer_list = list(masked_answer)
        for n in range(0, answer.count(char)):
            masked_answer_list[index] = char
            masked_answer = "".join(masked_answer_list)
            if n != answer.count(char) - 1:
                index = (answer.index(char, index + 1))
    else:
        attempt -= 1
        print("That letter doesn't appear in the word.")

    if masked_answer == answer:
        is_ended = True
        print("You guessed the word {}!".format(answer))
        print("You survived!")
        win += 1


def choice():
    flag = 1
    global is_ended, answer, masked_answer, user_input_set, attempt
    while flag:
        choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ')
        if choice == 'play':
            reset()
            is_ended = False
            flag = 0
            return True
        elif choice == 'results':
            print("You won: {} times.".format(win))
            print("You lost: {} times.".format(lose))
        elif choice == 'exit':
            flag = 0
            return False


def reset():
    global answer, masked_answer, user_input_set, attempt
    answer = answer_list[random.randint(0, 3)]
    masked_answer = "-" * (len(answer))
    user_input_set = []
    attempt = 8


# main
global userInput
print_title()
while choice():
    while attempt > 0 and not is_ended:
        global masked_answer
        print()
        print(masked_answer)
        user_input()
    if not is_ended:
        print()
        print("You lost!")
        lose += 1
