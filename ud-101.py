import pandas

df1 = pandas.read_csv("supermarkets.csv")

df1 = df1.set_index("Address")
#print(df1)


#df1_lim =df1.loc["735 Dolores St":"1056 Sanchez St","ID":"City"]
#print(df1_lim)


#df1_intercep = df1.loc["1056 Sanchez St","State"]
#print(df1_intercep)

"""
#only want everything in country
df1_USA = df1.loc[:,"Country"]
print(df1_USA)


#convert everything to a list
lis_usa = list(df1.loc[:,"Country"])
print(lis_usa)
"""

"""
#row , column
#row = 735 to3995
#column = City to Country
df1 = df1.iloc[1:3,1:3]
print(df1)
"""

#index 3 , Name 
df1 = df1.ix[3,"Name"]
print(df1)
