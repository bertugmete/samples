import pandas as pd , string , re

dataFrame = pd.read_excel("C:\\Users\\Bertug\\Desktop\\example.xlsx")

validation = ['.',':']

chars_to_remove = ['.', ',', '?','*','-','/']

dd = {ord(c):" " for c in chars_to_remove}

names1 = dataFrame.Name.str.translate(dd)

names2 = names1.str.capitalize()

names3 = names2.replace('\s+', ' ', regex=True)

print(names3)