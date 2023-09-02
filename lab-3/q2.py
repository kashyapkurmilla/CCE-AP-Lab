def uniqueList(l1):
    l2 = []
    for i in l1:
        if i in l2:
            continue
        else:
            l2.append(i)
    return l2


def main():
    l1 = []
    l2 = []
    n = int(input("Enter number of elements in the list :"))
    for i in range(n):
        temp = int(input(">"))
        l1.append(temp)
    print(l1)
    l2 = uniqueList(l1)
    print(l2)


main()
