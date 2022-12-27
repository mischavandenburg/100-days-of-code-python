# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

starting_letter_path = "./Input/Letters/starting_letter.txt"
names_path = "./Input/Names/invited_names.txt"
output_path = "./Output/ReadyToSend/"


def read_file(path):
    with open(path) as f:
        return f.readlines()


# get a list of the names
names = read_file(names_path)
# get all the lines of the letter in a list
starting_letter = read_file(starting_letter_path)

# loop over the names
for name in names:
    name = name.strip()
    filename = f"{name}.txt"
    # format the first line of the letter
    first_line = starting_letter[0].replace("[name]", name)

    new_letter = []
    # loop over the letter template and replace the first index with the
    # newly created first line

    for line in starting_letter:
        if starting_letter.index(line) == 0:
            line = first_line
        new_letter.append(line)

    new_letter_path = output_path + filename

    # write the new letter to a new file
    with open(new_letter_path, 'w') as f:
        for i in new_letter:
            f.write(i)
