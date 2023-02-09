# to remove even numbers

l1 = [12,3,2,876,35,25,11,76,90,11]
length1 = len(l1)
i=0
j=0
eve= []
while i<length1:
    if l1[i]%2==0:
        eve.append(l1[i])
    i+=1
print(eve)
length2 = len(eve)
while j<length2:
    l1.remove(eve[j])
print(l1)