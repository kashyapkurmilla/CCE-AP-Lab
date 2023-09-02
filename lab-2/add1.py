import sys


def calculate_square(x):
    return x ** 2


cache = {}


def cached_square(x):
    if x in cache:
        return cache[x]
    else:
        result = calculate_square(x)
        cache[x] = result
        return result


def main():
    while True:
        print('1. Square of a number')
        print('2. Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            n = int(input('Enter number: '))
            sqr = cached_square(n)
            print(sqr)
        elif choice == 2:
            sys.exit(0)
        else:
            print('Invalid choice,choose 1 or 2.')


main()
