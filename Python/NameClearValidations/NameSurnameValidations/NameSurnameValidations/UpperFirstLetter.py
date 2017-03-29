import pandas as pd , string , re

dataFrame = pd.read_excel("C:\\Users\\Bertug\\Desktop\\example.xlsx")

names1 = dataFrame.Name.str.lower().str.capitalize()

print(names1)