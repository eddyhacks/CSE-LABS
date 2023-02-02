# to demonstrate list functions and operations

list1 = [3,'john',3,'helloworld',6.6,3,'1212']
unsortlist = [5,9,1,3,6,8,2,0,23,876,13456.356]

print(list1)

# append
list1.append('12')
print(list1)

# copying
list2 = list1.copy()
print(list2)

# remove
list1.remove(3)
print(list1)

#insert
list1.insert(2,32)
print(list1)

# pop
list1.pop()
print(list1)

#count
len = list1.count(3)
print(len)

#reverse
list1.reverse()
print(list1)

#sort
unsortlist.sort()
print(unsortlist)


#index
value = list1.index(6.6)
print(value)

#extend
unsortlist.extend(list1)
print(unsortlist)

# clear
list1.clear()
print(list1)

