import array

storage = []
count = 0
 

# nhập mảng, tìm số chẵn, gán số âm bằng 0
a = int(input("number of input: \n"))
for c in range(0,a,1): 
    x = int(input(" input number: \n"))
    storage.append(x)

print(storage)

for x in storage: 
    if (x % 2 == 0):
        print("even number is " + str(x))
    elif (x < 0): 
        print(str(x) + " is negative")
        storage[count] = 0
    count += 1

print("check 1 complete ")
print(storage)
print("\n")

# sắp xếp lại mảng từ lớn đến bé
countx = 0
county = 0
memo = 0
for x in storage: 
    for y in storage: 
        if (x >= y): 
            memo = storage[countx] 
            storage[countx] = storage[county]
            storage[county] = memo 
        county += 1
    county = 0
    countx += 1

print("check 2 complete")
print(storage)
