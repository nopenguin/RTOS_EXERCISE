import array

name = str(input("type your name : \n"))
count = 0
check = 0
out = ""
w_array = name.split()
print(w_array)

for x in w_array: 
    for y in w_array: 
        if (x == y): 
            check += 1
            if (check > 1): 
                w_array[count] = ""
                print(count)
    check = 0
    count += 1

w_array.remove("")
w_array.sort()
for z in w_array: 
    out = out + z + " "

print(w_array)
print(out)
