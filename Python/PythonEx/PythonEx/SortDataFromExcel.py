import pandas as pd , operator

dataFrame = pd.read_excel("C:\\Users\\Bertug\\Desktop\\example.xlsx")

print(dataFrame.sort_values(by = ['Name','Age','Grade']))