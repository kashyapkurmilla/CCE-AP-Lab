inputfile = open('file.txt', 'r')
lines = inputfile.readlines()
print(lines)
wc = 0
lc = 0
cc=0
print(cc)
for line in lines:
    words = line.split()
    for word in words:
        wc = wc + 1
        cc=cc+len(word)
print(wc)
print(cc)
