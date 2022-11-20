play_num = 0
name = ["John",
        "Jack"]
print("How many pencils would you like to use:")
while True:  # pencil checking
    try:
        while True:  # checking for above 0
            pencil_num = int(input())
            if pencil_num > 0:
                break
            else:
                print("The number of pencils should be positive!")
        break
    except ValueError:  # predicting int exception
        print("The number of pencils should be numeric")

print(f"Who will be the first ({name[0]}, {name[1]})")
while True:  # checking the player
    name_choice = input()
    if name_choice == "John":
        play_num = 0
        break
    elif name_choice == "Jack":
        play_num = 1
        break
    else:
        print("Choose between 'John' and 'Jack'")

while pencil_num > 0:  # Game keeps going until the number of pencils is 0
    print("|" * pencil_num)
    if play_num == 0:
        print(f"{name[play_num]}'s turn!")
    else:
        print(f"{name[play_num]}'s turn:")
    if play_num == 0:  # player's turn, we're always John
        while True:  # Loop that makes sure the input is correct
            try:
                pencil_num_sub = int(input())
                if pencil_num_sub not in range(1, 4):
                    print("Possible values: '1', '2', or '3'")
                elif pencil_num_sub > pencil_num:
                    print("Too many pencils were taken")
                else:
                    break
            except ValueError:
                print("Possible values: '1', '2', or '3'")
    else:  # "AI"
        if pencil_num % 4 == 0:
            pencil_num_sub = 3
        elif pencil_num % 4 == 1:
            pencil_num_sub = 1
        elif pencil_num % 4 == 2:
            pencil_num_sub = 1
        elif pencil_num % 4 == 3:
            pencil_num_sub = 2
        print(pencil_num_sub)
    pencil_num -= pencil_num_sub
    play_num += 1
    play_num %= 2  # lazy way to alternate between players
print(f"{name[play_num]} won!")
