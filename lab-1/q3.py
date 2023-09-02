def main():
    # global k
    n = int(input("Enter number of strings :"))
    l1 = []
    l2 = []
    count1 = 0
    count2 = 0
    for i in range(n):
        temp = input(">")
        l1.append(temp)
    for i in l1:
        if i[0] == i[-1]:
            print(i[0], i[-1])
            count1 = count1 + 1
        k = len(i)
        if k > 2:
            count2 = count2 + 1
        if k % 2 == 1:
            l2.append(i)
    print("no of strings with same first and letters :", count1)
    print("no of strings with length>2 :", count2)
    print("strings with odd length",l2)


main()
