def calcCases(s):
    low = 0
    up = 0
    for i in range(len(s)):
        if s[i].islower():
            low = low + 1
        if s[i].isupper():
            up = up + 1
    print('upper case :', up)
    print('lower case :', low)


def main():
    s = input("Enter string:")
    calcCases(s)


main()
