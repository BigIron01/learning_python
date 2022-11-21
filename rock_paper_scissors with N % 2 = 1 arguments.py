import random


class Game:

    def __init__(self):
        self.player = None
        self.computer = None
        self.score = 0
        self.bad_ending = []
        return

    def score_change(self, points):
        self.score += points
        return

    def print_rating(self):
        return f"Your rating: {self.score}"

    def player_score(self, player):
        print("Hello, " + player)
        with open("rating.txt", "r+") as rating:
            for person in rating:
                if player in person:
                    self.score += int(person.split(" ")[1])
        return f"Your rating: {self.score}"

    def game_defining_moment(self, player, computer):
        self.computer = computer
        self.player = player
        very_convenient_number = (len(rps) - 1) // 2
        for weakness in range(very_convenient_number):
            bad_ending.append(rps[(rps.index(self.player) + 1 + weakness) % len(rps)])
        if self.computer in bad_ending:
            return f"Sorry, but the computer chose {self.computer}"
        elif player_choice == self.computer:
            self.score += 50
            return f"There is a draw ({self.computer})"
        else:
            self.score += 100
            return f"Well done. The computer chose {self.computer} and failed"


game = Game()
player_name = input("Enter your name: ")  # TODO: maybe bring score as a class?
print(game.player_score(player_name))

rps = input()
print("Okay, let's start")
if not rps:
    rps = ["rock", "paper", "scissors"]
else:
    rps = rps.split(",")

while True:
    bad_ending = []
    computer_choice = random.choice(rps)
    while True:  # TODO: don't like that loop, rewrite it to a parameter instead
        player_choice = input()
        if player_choice in rps or player_choice == "!exit":
            break
        elif player_choice == "!rating":
            print(game.print_rating())
            break
        else:
            print("Invalid input")
    if player_choice == "!exit":
        break
    elif player_choice == "!rating":
        game.print_rating()
    else:
        print(game.game_defining_moment(player_choice, computer_choice))
print("Bye!")
