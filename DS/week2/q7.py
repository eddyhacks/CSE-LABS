import pandas as pd
data1  = {'Name':['Kavitha','Sudha','Raju','james','Alice']}
df1 = pd.DataFrame(data1)
data2 = {'Maths':[80.0,90.0,77.5,87.5,86.5],'physics':[81.0,94.0,74.5,83.0,82.5],'Chemistry':[91.5,86.5,85.5,90.0,91.0],'Biology':[82.5,83.5,84.5,85.0,93]}
df2 = pd.DataFrame(data2)

print("\n")
# df_vertical = pd.concat([df1,df2],axis=0)
df = pd.concat([df1,df2],axis=1)


# Total
df['total'] = df2.sum(axis=1)
print(df)