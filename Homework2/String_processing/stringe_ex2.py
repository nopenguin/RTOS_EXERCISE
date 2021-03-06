import array

name = str(input("type your name: \n"))
store = name.split()
right = 0
wrong = 0
print(store)

for x in store: 
    if (x[0].isupper()):
        right += 1
    elif (x[0].islower()): 
        wrong += 1

print("Đúng: " + str(right))
print("Sai: " + str(wrong))