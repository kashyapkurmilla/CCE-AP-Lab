def isArmstrong(num):
    original_number = num
    total = 0
    num_digits = len(str(num))

    while num > 0:
        digit = num % 10
        total += digit ** num_digits
        num //= 10

    return total == original_number


number = int(input("Enter a number: "))
if isArmstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
