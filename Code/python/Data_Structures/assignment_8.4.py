# Use the file name romeo.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    splt=line.split()
    for x in splt:
    	if x not in lst:
        	lst.append(x)

    
lst.sort()
print(lst)