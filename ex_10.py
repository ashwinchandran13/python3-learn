handler = open('mbox.txt')

count = dict()
for line in handler:
    if not line.startswith('From '):
        continue
    line = line.split()
    hourLine = line[5]
    hour = hourLine.split(':')
    count[hour[0]] = count.get(hour[0], 0) + 1
# long method
# tempList = list()

# for k,v in count.items():
#     tempList.append((v, k))

# temp = sorted(tempList)

# list comprehension

temp = sorted([(k, v) for k, v in count.items()]);

for key, value in temp:
    print(key, value)
