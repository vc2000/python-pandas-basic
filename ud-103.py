import pandas
df1 = pandas.read_csv("supermarkets.csv")

#add column
#df1["Continent"] =["North America","North America","North America","North America","North America","North America"]
#shape[row,columns]
df1["Continent"] = df1.shape[0]*["North America"]
df1=df1.set_index("Address")


#update Continent
df1["Continent"] = df1["Country"] + " , " + "North America"
#print(df1)
#print()



#----------------- add new row ---------------
#column become row , and row become columns
df1_t = df1.T

df1_t["Tuen Wan"] =["968135242","HK","NT","CH","Venus","Annie","CH"]
#print(df1_t)
df1 = df1_t.T
print(df1)
