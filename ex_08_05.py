fhand = open('mbox.txt')
count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    word = line.split()
    print(word)

print('There were',count,'lines in the file with From as the first word')