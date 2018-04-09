import pandas

df1 = pandas.read_csv("supermarkets.csv")
df1 = df1.set_index("Address")


#delet row, pass 0
#delet column , pass 1
df1=df1.drop("City",1)
print(df1)
