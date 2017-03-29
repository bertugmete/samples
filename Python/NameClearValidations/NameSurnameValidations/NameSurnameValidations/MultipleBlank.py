import pandas as pd , string , re

df = pd.read_excel("C:\\Users\\Bertug\\Desktop\\example.xlsx")

df.Name = df.Name.replace('\s+', ' ', regex=True)

print (df)