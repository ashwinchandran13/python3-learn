fname = input('Enter file name:')
try:
    fhandle = open(fname)
except:
    print('Invalid file name')
    quit()

count = 0
avgVar = 0

for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    spos = line.find(':')
    line = line[spos+1:].lstrip()
    floatLine = float(line)
    avgVar = avgVar + floatLine

print('Average spam confidence:', avgVar/count)