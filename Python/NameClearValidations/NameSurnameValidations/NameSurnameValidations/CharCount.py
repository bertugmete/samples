import pandas as pd , string , re

dataFrame = pd.read_excel("C:\\Users\\Bertug\\Desktop\\example.xlsx")

for data in dataFrame["Name"] :
    if data.value_counts < 2 :
        print("az")
    else :
        print("Cok")