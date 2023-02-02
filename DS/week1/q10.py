# print negative number using for loop

list1 = [11,-21,0,45,66,-93]

c_neg=0
c_pos=0
for i in list1:
    if i%2==0:
        list1.remove(i)

print(list1)
