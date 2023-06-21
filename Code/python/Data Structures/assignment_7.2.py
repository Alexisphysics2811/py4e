# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos1 = line.find(':')
    pos1 = pos1 + 2
    value = float(line[pos1:])
    count = count + 1
    total = total + value
avg = total/count
print('Average spam confidence:', avg)
