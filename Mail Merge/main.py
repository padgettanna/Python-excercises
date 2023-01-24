with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    for name in names:
        file_name = name.strip()
        new_content = content.replace("[name]", file_name)
        with open(f"./Output/ReadyToSend/letter_for {file_name}.txt", 'w') as file:
            file.write(new_content)
