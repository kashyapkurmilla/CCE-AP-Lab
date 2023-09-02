import random


def readNumbers():
    d = {}
    n = int(input('Enter no of elements in the dictionary: '))
    print('Enter numbers: ')
    for i in range(n):
        key = random.randrange(0, 100)
        value = int(input())
        d[key] = value
    print(d)
    avg = d_average(d)
    print('Average:', avg)


def d_average(d):
    total = 0
    for value in d.values():
        total += value
    if len(d) > 0:
        avg = total / len(d)
    else:
        avg = 0
    return avg


def main():
    readNumbers()


main()
