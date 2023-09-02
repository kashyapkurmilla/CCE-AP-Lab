def multiplyList(l1):
    totalProduct = 1
    for i in range(len(l1)):
        totalProduct = totalProduct * l1[i]
    print('Product of values in the list : ', totalProduct)


def main():
    l1 = []
    n = int(input("Enter number of elements in the list :"))
    for i in range(n):
        temp = int(input(">"))
        l1.append(temp)
    print(l1)
    multiplyList(l1)


main()
