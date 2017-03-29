import pandas as pd , string , re

dataFrame = pd.read_excel("C:\\Users\\Bertug\\Desktop\\example.xlsx")

validation = ['.',':']

chars_to_remove = ['.', ',', '?']

dd = {ord(c):" " for c in chars_to_remove}

names1 = dataFrame.Name.str.translate(dd)
print(names1)