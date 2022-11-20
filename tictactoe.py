def fact_checker():
    for i in range(3):
        if len(set(grid[(3 * i):3 * i + 3:])) == 1:  # counts each horizontal solution and stores it
            if grid[3 * i] == "O" or grid[3 * i] == "X":
                winning.append(grid[3 * i])
    for i in range(3):
        if len(set(grid[i::3])) == 1:  # counts each vertical solution and stores it
            if grid[i] == "O" or grid[i] == "X":
                winning.append(grid[i])
    if len(set(grid[::4])) == 1:
        if grid[4] == "O" or grid[4] == "X":
            winning.append(grid[4])
    if len({grid[2], grid[4], grid[6]}) == 1:
        if grid[2] == "O" or grid[2] == "X":
            winning.append(grid[2])
    if len(winning) > 0:
        print(f"{winning[0]} wins")
        return True
    elif exes + texas == 9 and winning == []:
        print("Draw")
        return True
    else:
        return False


def game_draw():
    print("---------")
    print(f"| {grid[0]} {grid[1]} {grid[2]} |")
    print(f"| {grid[3]} {grid[4]} {grid[5]} |")
    print(f"| {grid[6]} {grid[7]} {grid[8]} |")
    print("---------")


grid = [" " for _ in range(9)]
del grid[9::]
for j in range(9):
    if grid[j] == "_":
        grid[j] = " "
winning = []
player = 0
while True:
    game_draw()
    exes = grid.count("X")
    texas = grid.count("O")
    new_move = input().split()
    try:
        choice = ((int(new_move[0]) - 1) * 3) + int(new_move[1]) - 1
    except ValueError:
        print("You should enter numbers!")
    else:
        if int(new_move[0]) not in range(4) or int(new_move[1]) not in range(4):
            print("Coordinates should be from 1 to 3!")
        elif grid[choice] == "X" or grid[choice] == "O":
            print("This cell is occupied! Choose another one!")
        else:
            if player == 0:
                grid[choice] = "X"
            else:
                grid[choice] = "O"
    game_draw()
    if fact_checker():
        break
    else:
        pass
    player += 1
    player %= 2
