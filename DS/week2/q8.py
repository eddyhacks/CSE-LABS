import pandas as pd
data1  = {'Name':['Kavitha','Sudha','Raju','james','Alice'],'Quiz1':[80.0,90.0,77.5,87.5,86.5],'Insem1':[81.0,94.0,74.5,83.0,82.5],'Quiz2':[91.5,86.5,85.5,90.0,91.0],'Insem2':[82.5,83.5,84.5,85.0,93]}
df1 = pd.DataFrame.from_dict(data1)
# df_vertical = pd.concat([df1,df2],axis=0)
# Total
df1['total'] = df1.sum(axis=1)
df1.loc['mean'] = df1.mean(axis=0)

print(df1)