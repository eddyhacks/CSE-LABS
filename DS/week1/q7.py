tupl = (12,7,38,56,78)
length = len(tupl)

tupl1 = list()
for i in tupl:
    if i%2==0:
        tupl1.append(i)
tp2 = tuple(tupl1)
print(tp2)