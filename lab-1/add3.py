def ishexadecimal(s):
    s = s.upper()
    valid_hex_digits = set("0123456789ABCDEF")
    for char in s:
        if char not in valid_hex_digits:
            return False

    return True


input_string = input("Enter a string: ")

if ishexadecimal(input_string):
    print(input_string + " is a hexadecimal number.")
else:
    print(input_string + " is not a hexadecimal number.")
