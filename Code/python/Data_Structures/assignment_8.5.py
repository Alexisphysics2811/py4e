# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1 :
	fname = "mbox-short.txt"

fh = open(fname)
lst = list()
count = 0

for line in fh:
    sub = line.find('From')
    sub2 = line.find('From:')
    if (sub != -1):
    	if (sub2 == -1):
            splt = line.split()
            email = splt[sub+1]
            lst.append(email)
            print(email)


count = len(lst)
print("There were", count, "lines in the file with From as the first word")
