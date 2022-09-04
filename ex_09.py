
handler = open('mbox.txt')

count = dict()

for line in handler:
    if not line.startswith('From'):
        continue
    line = line.split()
    count[line[1]] = count.get(line[1], 0) + 1

greatestname = None
greatestcount = None

for name, count in count.items():
    if greatestcount is None or count > greatestcount:
        greatestcount = count
        greatestname = name

print(greatestname, greatestcount)