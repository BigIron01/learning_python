import random


def shuffle():
    stock_pieces = []
    for i in range(7):
        for j in range(7 - i):
            stock_pieces.append([i, j + i])
    player_1 = []
    player_2 = []
    for i in range(7):
        player_1.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
    for i in range(7):
        player_2.append(stock_pieces.pop(random.randint(0, len(stock_pieces) - 1)))
    return player_1, player_2, stock_pieces


def domino_snake(player_1, player_2):
    gamers = [player_1, player_2]
    gamer_highest = []
    gamer_record = []
    for i in range(2):
        for j in range(len(gamers[0])):
            if gamers[i][j][0] == gamers[i][j][1]:
                if gamers[i][j] > gamer_record:
                    gamer_record = gamers[i][j]
            else:
                pass
        if len(gamer_record) > 0:
            gamer_highest.append([i, gamer_record])
        elif not gamer_record:
            pass
        gamer_record = []
    return gamer_highest  # so yeah, export the final values, domino snake and the player number


def first_player_selection(gamer_highest):
    if len(gamer_highest) == 2:
        if gamer_highest[0][1][0] > gamer_highest[1][1][0]:
            selected_man = 0
        else:
            selected_man = 1
    elif len(gamer_highest) == 1:
        selected_man = gamer_highest[0][0]
    else:
        selected_man = 2
    return selected_man


shuffler = 0
selected_boi = 0
game_valid = True
correct_input = False
starting_domino = []
while not starting_domino:
    shuffler = shuffle()
    gamer = domino_snake(shuffler[0], shuffler[1])
    selected_boi = first_player_selection(gamer)
    if len(gamer) == 2:
        if gamer[0][0] == selected_boi:
            starting_domino = [shuffler[0].pop(shuffler[0].index(gamer[0][1]))]
        elif gamer[1][0] == selected_boi:
            starting_domino = [shuffler[1].pop(shuffler[1].index(gamer[1][1]))]
        else:
            starting_domino = []
    elif len(gamer) == 1:
        starting_domino = [shuffler[selected_boi].pop(shuffler[selected_boi].index(gamer[0][1]))]
while game_valid:
    print("="*70)
    print(f"Stock size: {len(shuffler[2])}")
    print(f"Computer pieces: {len(shuffler[1])}")
    print()
    if len(starting_domino) in range(6):
        for _ in range(len(starting_domino)):
            print(f"{starting_domino[_]}", end="")
    else:
        for _ in range(3):
            print(f"{starting_domino[_]}", end="")
        print("...", end="")
        for _ in range(0, 3):
            print(f"{starting_domino[-3+_]}", end="")
    print()
    print()
    print("Your pieces:")
    for _ in range(len(shuffler[0])):
        print(f"{_ + 1}:{shuffler[0][_]}")
    print()
    if len(shuffler[0]) == 0:  # TODO: you could separate that for clarity, moves and checks I suppose
        print("Status: The game is over. You won!")
        game_valid = False
        selected_boi += 2
    elif len(shuffler[1]) == 0:
        print("Status: The game is over. The computer won!")
        game_valid = False
        selected_boi += 2
    if starting_domino[0][0] == starting_domino[-1][1] and game_valid:
        draw_condition = 0
        for _ in range(len(starting_domino)):
            first_list = [inner_list[0] for inner_list in starting_domino]
            second_list = [inner_list[1] for inner_list in starting_domino]
            draw_condition = first_list.count(starting_domino[0][0])
            draw_condition += second_list.count(starting_domino[0][0])
        if draw_condition >= 8:
            print("Status: The game is over. It's a draw!")
            game_valid = False
            selected_boi += 2
    if selected_boi == 0:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        command = input()
    elif selected_boi == 1:
        print("Status: It's your turn to make a move. Enter your command.")
    if selected_boi == 1:
        correct_input = False
        while not correct_input:
            try:
                command = int(input())
                if command == 0:
                    if len(shuffler[2]) > 0:
                        shuffler[0].append(shuffler[2].pop(random.randint(0, (len(shuffler[2]) - 1))))
                    correct_input = True
                elif command > 0 and command in range(len(shuffler[0]) + 1):
                    if shuffler[0][command - 1][0] == starting_domino[- 1][1]:
                        starting_domino.append(shuffler[0].pop(command - 1))
                        correct_input = True
                    elif shuffler[0][command - 1][1] == (starting_domino[- 1][1]):
                        starting_domino.append(shuffler[0].pop(command - 1)[::-1])
                        correct_input = True
                    else:
                        print("Illegal move. Please try again.")
                        correct_input = False
                elif command < 0 and abs(command + 1) in range(len(shuffler[0]) + 1):
                    if shuffler[0][abs(command) - 1][0] == starting_domino[0][0]:
                        starting_domino.insert(0, shuffler[0].pop(abs(command) - 1)[::-1])
                        correct_input = True
                    elif shuffler[0][abs(command) - 1][1] == (starting_domino[0][0]):
                        starting_domino.insert(0, shuffler[0].pop(abs(command) - 1))
                        correct_input = True
                    else:
                        print("Illegal move. Please try again.")
                        correct_input = False
                else:
                    print("Invalid input. please try again.")
            except ValueError:
                print("Invalid input. please try again.")
    elif selected_boi == 0:
        domino_lib = {0: 0,
                      1: 0,
                      2: 0,
                      3: 0,
                      4: 0,
                      5: 0,
                      6: 0}
        domino_score = {}
        for elements in range(len(starting_domino)):
            for parts in range(2):
                domino_lib[starting_domino[elements][parts]] += 1
        for elements in range(len(shuffler[1])):
            domino_score[elements] = domino_lib[shuffler[1][elements][0]] + domino_lib[shuffler[1][elements][1]]
        choice_order = sorted(domino_score, key=domino_score.get)
        correct_input = False
        for _ in choice_order:
            if shuffler[1][_][0] == starting_domino[0][0]:
                starting_domino.insert(0, shuffler[1].pop(_)[::-1])
                correct_input = True
                break
            elif shuffler[1][_][1] == starting_domino[0][0]:
                starting_domino.insert(0, shuffler[1].pop(_))
                correct_input = True
                break
            elif shuffler[1][_][1] == starting_domino[0][0]:
                starting_domino.append(shuffler[1].pop(_))
                correct_input = True
                break
            elif shuffler[1][_][1] == starting_domino[0][0]:
                starting_domino.append(shuffler[1].pop(_)[::-1])
                correct_input = True
                break
        if not correct_input:
            if len(shuffler[2]) > 0:
                shuffler[1].append(shuffler[2].pop(random.randint(0, (len(shuffler[2]) - 1))))
    selected_boi += 1
    selected_boi = selected_boi % 2
