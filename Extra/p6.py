inputfile = open('file.txt','r+',encoding='utf-8')
lines = inputfile.readlines()
lines.reverse()
print(lines)
inputfile.truncate()
inputfile.seek(0)
for line in lines:
    words = line.split()
    for word in words:
        inputfile.write(word+' ')
    inputfile.write('\n')
inputfile.close()
