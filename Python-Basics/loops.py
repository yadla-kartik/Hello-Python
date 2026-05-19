print('There are 2 types of loops in python - for loop and while loop')

list = [1,2,3,4,5]
for el in list:
    print(el)

print('------------------Using while loop-----------------')

i = 0
while(i < len(list)):
    print(list[i])
    i += 1

print('------------------Using for loop with range()-----------------')

for i in range(1, 6, 1):
    print(i) 

print('------------------Using range() to print table-----------------')

for i in range(5, 51, 5):
    print(i)