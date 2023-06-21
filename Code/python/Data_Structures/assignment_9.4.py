# Use the file name mbox-short.txt as the file name
name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
lst = list()
email = None

for line in handle:
    words = line.split
    sub = line.find('From')
    sub2 = line.find('From:')
    if sub != -1:
        if sub2 == -1:
            splt = line.split()
            email = splt[sub+1]
            lst.append(email)


for mail in lst:
	if mail not in counts:
		counts[mail] = 1
	else:
		counts[mail] = counts[mail]+1

bigcount = None
bigword = None

for mail, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = mail
        bigcount = count
        
print(bigword, bigcount)
