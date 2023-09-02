def countWords(str):
    d = dict()
    n = str.split()
    print(n)
    for word in n:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    print(d)


def main():
    str = input("Enter String :")
    countWords(str)


main()
