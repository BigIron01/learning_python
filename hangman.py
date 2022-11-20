import random
import string

print("H A N G M A N")
game_wins = 0
game_losses = 0
while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    print("")
    decision = input()
    if decision == "play":
        possible_answers = ("python", "java", "swift", "javascript")
        answer_random = random.randint(0, (len(possible_answers) - 1))
        answer_correct = possible_answers[answer_random]
        letters_unknown = set(answer_correct)
        already_guessed = set()
        victory = False
        i = 0
        while True:
            letters_unknown.discard(already_guessed)
            hint = list(answer_correct)
            for j in range(len(hint)):
                if answer_correct[j] in letters_unknown:
                    hint[j] = "-"
                else:
                    pass
            hint = "".join(hint)
            print(hint)
            letter_guessed = input("Input a letter: ")
            if len(letter_guessed) != 1:
                print("Please, input a single letter.")
            elif letter_guessed not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter_guessed in already_guessed:
                print("You've already guessed this letter.")
                already_guessed.add(letter_guessed)
                i += 1
            elif letter_guessed in set(answer_correct):
                letters_unknown.discard(letter_guessed)
                already_guessed.add(letter_guessed)
            else:
                print("That letter doesn't appear in the word.")
                already_guessed.add(letter_guessed)
                i += 1
            print("")
            if i == 8:
                break
            if letters_unknown == set():
                victory = True
                break
        if victory:
            print(f"You guessed the word {answer_correct}!")
            print("You survived!")
            game_wins += 1
        else:
            print("You lost!")
            game_losses += 1
    elif decision == "results":
        print(f"You won: {game_wins} times")
        print(f"You lost: {game_losses} times")
    elif decision == "exit":
        break
