#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('./Input/Letters/starting_letter.txt', 'r') as f:
    letter = f.read()

with open('./Input/Names/invited_names.txt', 'r') as f:
    names = f.readlines()

    for n in names:
        name = n.strip()
        new_letter = letter.replace('[name]', name)

        with open(f'./Output\ReadyToSend/{name}.txt', 'w') as f:
            f.write(new_letter)
