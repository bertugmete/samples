import pandas as pd

dataFrame = pd.read_excel("C:\\Users\\Bertug\\Desktop\\example.xlsx")

#print(dataFrame.duplicated('Name'))

#print(dataFrame.duplicated('Grade'))

print(dataFrame.set_index('Name').index.get_duplicates())

#print(dataFrame.duplicated('Name').value_counts())

#print(dataFrame.set_index('Name').index.drop_duplicates())