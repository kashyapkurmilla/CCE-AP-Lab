import math


def main():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    for count in range(n, m + 1):
        isprime = True

        for x in range(2, int(math.sqrt(count)) + 1):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            print(count)


main()