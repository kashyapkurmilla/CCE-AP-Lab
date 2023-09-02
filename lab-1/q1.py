l1 = []
l2 = []
l3 = []
n = int(input("Enter number of elements : "))
print('Enter elements to append in list one :')
for i in range(n):
    temp = int(input(">"))
    l1.append(temp)
print('Enter elements to append in list two :')
for i in range(n):
    temp = int(input(">"))
    l2.append(temp)
for i in l1:
    if i % 2 == 1:
        l3.append(i)
for i in l2:
    if i % 2 == 0:
        l3.append(i)
print(l3)
