# swap the values of two variables

a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))

# swap the vaues
print("\nbefore the swap:",a,b)
temp =a
a=b
b=temp

print("after the swap:",a,b)