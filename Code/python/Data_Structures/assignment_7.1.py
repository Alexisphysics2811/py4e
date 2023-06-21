# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fs = fh.read()
fss = fs.strip()
fssup = fss.upper()
print(fssup)