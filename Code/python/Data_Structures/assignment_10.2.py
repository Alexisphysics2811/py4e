# Use the file name mbox-short.txt as the file name
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
lst = list()
lst2 = list()

for line in handle:
    sub = line.find('From')
    sub2 = line.find('From:')
    if sub != -1:
        if sub2 == -1:
            splt = line.split()
            time = splt[sub+5]
            hour = time.split(':')
            lst.append(hour[0])

for hr in lst:
	if hr not in counts:
		counts[hr] = 1
	else:
		counts[hr] = counts[hr]+1

lst2 = sorted(counts.items())

for k,v in lst2:
    print(k,v)