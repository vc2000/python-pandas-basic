import pandas

"""
#need [] to contain all data
df1= pandas.DataFrame([[2,4,6],[10,20,30]])
print(df1)
print()

df2 = pandas.DataFrame([[2,4,6],[1,2,3]],columns = ['Price','Age','Value'])
print(df2)
print()
"""
df3 = pandas.DataFrame([[2,4,6],[1,2,3]],columns = ['Price','Age','Value'], index= ["1st",'2nd'])
print(df3)
print()

#df4 = pandas.DataFrame([{"Name":"John","Last":"chu"},{"Name":"Venus","Last":"Smart"}])
#print(df4)

#######################################################
#print(df3)
#print(type(df3))

#check methods
#print(dir(df3))

mean= df3.mean()
print(mean)
print()

fage = df3.Age
print(fage)
print()

max = df3.Price.max()
print(max)
