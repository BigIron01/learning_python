msg_ = ["Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]


def dissing_user(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and (is_one_digit(v2)):
        msg = msg + msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":  # checking for multiplying by one
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


def is_one_digit(v1):
    if (-10 < v1 < 10) and v1.is_integer():
        return True


def are_you_sure_about_that(result_m):
    global sept_21
    index = 10
    if is_one_digit(result_m):
        decision = "y"
        while index < 13 and decision == "y":
            if is_one_digit(result_m):
                print(msg_[index])
                decision = input()
                index += 1
    else:
        sept_21 = result_m
    if index == 13:
        sept_21 = result_m


i = False  # "i" is the end of the loop checking for errors
result = 0
cont_calc = "y"
i_2 = True
sept_21 = 0

while cont_calc == "y":
    while i is not True:  # Loop responsible for checking for errors
        while True:  # Endless loop for msg_1 - input proper value until you get it right
            try:
                print(msg_[0])
                calc = input()
                calc = calc.split()
                if calc[0] == "M":  # checks if M, otherwise proceeds as it did earlier
                    a = sept_21
                else:
                    a = calc[0]
                if calc[2] == "M":
                    b = sept_21
                else:
                    b = calc[2]
                a = float(a)
                b = float(b)
                break
            except ValueError:
                print(msg_[1])
        calculation = calc[1]
        # dissing people be like
        dissing_user(a, b, calculation)
        # dissing people be like
        if calculation == "/":  # checking calculations, correct calculation ends the "i" loop
            try:
                result = (a / b)
            except ZeroDivisionError:
                print(msg_[3])
            else:
                i = True
        elif calculation == "*":
            i = True
            result = (a * b)
        elif calculation == "-":
            i = True
            result = (a - b)
        elif calculation == "+":
            i = True
            result = (a + b)
        else:
            print(msg_[2])
    print(result)
    print(msg_[4])
    do_you_remember = input()
    if do_you_remember == "y":  # comedy genius
        are_you_sure_about_that(result)
    else:
        sept_21 = 0
    print(msg_[5])
    cont_calc = input()
    i_2 = True  # resets the loop
    i = False  # resets the loop
