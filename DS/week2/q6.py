import pandas as pd
data  = {'Name':['Kavitha','Sudha','Raju','Vignesh'],'Height':[5.4,6,5,5.2],'Qualification':["B.tech","M.tech","BSC","MS"]}
df = pd.DataFrame(data,index = ['1','2','3','4'])
print(df)
df.insert(1,"newCol",[1,2,3,4])
print(df)