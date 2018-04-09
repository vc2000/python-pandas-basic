import pandas

#--------------------------csv-----------------------------------
"""
df1 = pandas.read_csv("supermarkets.csv")


# telling python that this csv file doesn't has header
df2 = pandas.read_csv("supermarkets.csv", header = None)
print(df2)

#use ID as index
new = df1.set_index('ID')
#print(new)

#6 rows 7 columns
#print(df1.shape)

"""
#--------------------------json-----------------------------
"""
df3 = pandas.read_json("supermarkets.json")
new_df3= df3.set_index("ID")
print(new_df3.shape)
"""

#-------------------------xlsx----------------------------
"""
df4 = pandas.read_excel("supermarkets.xlsx",sheetname = 0)
print(df4)
"""

#-------------------------txt---------------------------
"""
df5 = pandas.read_csv("supermarkets-commas.txt")
print(df5)
"""
#ask questions - pandas.read?
df6 = pandas.read_csv("supermarkets-semi-colons.txt",sep = ";")
print(df6)
