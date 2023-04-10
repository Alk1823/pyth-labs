
numberlist = []
for i in range(10):
    num = float(input("Enter number:"))
    numberlist.insert(i,num)

largest = numberlist[0]

for i in range(1,10):
    if largest < numberlist[i]:
        largest = numberlist[i]

print(largest)