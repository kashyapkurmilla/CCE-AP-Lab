def main():
    # Get text content from the user
    lines = []
    while True:
        line = input("Enter a line of text (-1 to exit): ")
        if line == '-1':
            break
        lines.append(line)

    with open("sample.txt", "w") as file:
        for line in lines:
            file.write(line + '\n')

    with open("sample.txt", "r") as file:
        lines = file.readlines()

    line_data_dict = {}
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        line_length = len(line)
        line_data_dict[line_number] = [line, line_length]

    print("Dictionary with line numbers as keys and [string, length] as values:")
    print(line_data_dict)

    letter_frequency_dict = {}
    for line in lines:
        for char in line:
            if char.isalpha():
                char_lower = char.lower()
                if char_lower in letter_frequency_dict:
                    letter_frequency_dict[char_lower] += 1
                else:
                    letter_frequency_dict[char_lower] = 1

    print("\nDictionary with letter frequencies:")
    print(letter_frequency_dict)


main()
