class CoffeeMachine:

    def __init__(self, water, milk, c_beans, cups, money):
        self.coffee_machine_current = {"water": water, "milk": milk, "c_beans": c_beans, "cups": cups, "money": money}
        self.ingredients = {"espresso": {"water": 250, "milk": 0, "c_beans": 16, "cups": 1, "money": -4},
                            "latte": {"water": 350, "milk": 75, "c_beans": 20, "cups": 1, "money": -7},
                            "cappuccino": {"water": 200, "milk": 100, "c_beans": 12, "cups": 1, "money": -6}}
        self.coffee_type = {1: "espresso", 2: "latte", 3: "cappuccino"}
        self.ingredients_name = {"water": "water", "milk": "milk,", "c_beans": "coffee beans", "cups": "cups"}

    def __str__(self):
        return (f"The coffee machine has: \n"
                f"{self.coffee_machine_current['water']} ml of water \n"
                f"{self.coffee_machine_current['milk']} ml of milk \n"
                f"{self.coffee_machine_current['c_beans']} g of coffee beans \n"
                f"{self.coffee_machine_current['cups']} disposable cups \n"
                f"${self.coffee_machine_current['money']} of money \n")

    def refill(self, added_water, added_milk, added_c_beans, added_cups):
        self.coffee_machine_current["water"] += added_water
        self.coffee_machine_current["milk"] += added_milk
        self.coffee_machine_current["c_beans"] += added_c_beans
        self.coffee_machine_current["cups"] += added_cups
        return

    def buy(self, coffee_selection):
        empty_machine = False
        missing_ingredient = False
        coffee_selection = int(coffee_selection)
        for key in self.coffee_machine_current:
            if self.coffee_machine_current[key] - self.ingredients[self.coffee_type[coffee_selection]][key] < 0:
                missing_ingredient = key
                empty_machine = True
                break
        if not empty_machine:
            print("I have enough resources, making you a coffee!")
            for key in self.coffee_machine_current:
                self.coffee_machine_current[key] -= self.ingredients[self.coffee_type[coffee_selection]][key]
        else:
            print(f"Sorry, not enough {self.ingredients_name[missing_ingredient]}")
        return

    def take(self):
        money_stolen = self.coffee_machine_current["money"]
        self.coffee_machine_current["money"] = 0
        return f"I gave you ${money_stolen}"


brush_up = CoffeeMachine(400, 540, 120, 9, 550)  # I really didn't know how to name this instance
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    user_action = input()
    print()
    if user_action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_selected = input()
        if coffee_selected == "back":
            pass
        else:
            brush_up.buy(int(coffee_selected))
    elif user_action == "fill":
        print("Write how many ml of water you want to add::")
        add_water = int(input())  # I know it's not funny anymore, but I couldn't resist
        print("Write how many ml of milk you want to add:")
        add_milk = int(input())
        print("Write how many grams of coffee beans you want to add")
        add_c_beans = int(input())
        print("Write how many disposable cups you want to add:")
        add_cups = int(input())
        brush_up.refill(add_water, add_milk, add_c_beans, add_cups)
    elif user_action == "take":
        print(brush_up.take())
    elif user_action == "exit":
        break
    elif user_action == "remaining":
        print(brush_up)
    print()
