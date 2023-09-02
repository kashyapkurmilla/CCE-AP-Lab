list1 = list(map(int, input("enter list1:").split()))
list2 = list(map(int, input("enter list2:").split()))


def uni(list1, list2):
    union = []
    for i in list1:
        if i not in union:
            union.append(i)
    for i in list2:
        if i not in union:
            union.append(i)
    return union


def inter(list1, list2):
    intersection = []
    for i in list1:
        if i in list2 and i not in intersection:
            intersection.append(i)
    return intersection


def diff(list1, list2):
    difference = []
    for i in list1:
        if i not in list2 and i not in difference:
            difference.append(i)
    return difference


uni_result = uni(list1, list2)
inter_result = inter(list1, list2)
diff_result = diff(list1, list2)

print("Union:", uni_result)
print("Intersection:", inter_result)
print("Difference:", diff_result)
