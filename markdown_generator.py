functions = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]
commands = ["!help", "!done"]
output = []

while True:
    while True:
        command = input("Choose a formatter: ")
        if command in (*functions, *commands):
            break
        else:
            print("Unknown formatting type or command")
    if command == "!help":
        print(f"Available formatters: {' '.join(functions)}")
        print(f"Special commands: {' '.join(commands)}")
    elif command == "!done":
        break
    elif command == "header":
        while True:
            header_level = int(input("Level: "))
            if header_level not in range(1, 7):
                print("The level should be within the range of 1 to 6")
            else:
                break
        text = input("Text: ")
        output.append("#" * header_level + " " + text + "\n")
    elif command in ("plain", "bold", "italic", "inline-code"):
        text = input("Text: ")
        if command == "plain":
            output.append(text)
        elif command == "bold":
            output.append("**" + text + "**")
        elif command == "italic":
            output.append("*" + text + "*")
        else:
            output.append("`" + text + "`")
    elif command == "new-line":
        output.append("\n")
    elif command == "link":
        label = input("Label: ")
        link = input("URL: ")
        output.append(f"[{label}]({link})")
    elif command in ("ordered-list", "unordered-list"):
        while True:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
            print("The number of rows should be greater than zero")
        output.extend([f"{index}. {input(f'Row #{index}: ') }\n"
                       if command == "ordered-list" else f"* {input(f'Row #{index}: ')}\n"
                       for index in range(1, rows + 1)])
    print("".join(output))

with open("output.md", "wt") as file:
    file.write("".join(output))
