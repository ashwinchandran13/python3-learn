fhand = open('romeo.txt')
arrlist = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in arrlist:
            arrlist.append(word)

arrlist.sort()
print(arrlist)