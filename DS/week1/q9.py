# print negative number using for loop

list1 = [11,-21,0,45,66,-93]

c_neg=0
c_pos=0
for i in list1:
    if i<0:
        c_neg = c_neg+1
    else:
        c_pos = c_pos+1
print("The number of negative numbes: ",c_neg,"\nThe number of positive nubmers",c_pos)
