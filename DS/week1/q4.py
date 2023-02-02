# find the largest among these

a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))
c = int(input("Enter the c value: "))

# finding largest using if else
'''
max = a
if a<b:
    if b<c:
        max=c
    else:
        max=b
else:
    if c>a:
        max=c
    else:
        max=a

print("The maximum is:",max)
'''
# the other way

if a>b and a>c:
    max=a
elif b>a and b>c:
    max=b
else:
    max=c

print(max)