import pandas as pd

ufo = pd.read_csv("http://bit.ly/uforeports")


# scv olarak ayrilan dosyalar icin tail ile kaybolan veriler yerine Nan yazabiliriz.

#print(ufo.tail())

#print(ufo.isnull().tail())

#print(ufo.notnull().tail())

#bos olmayanlarin sayisini elde etmek.
#print(ufo.isnull().sum())

#print(pd.Series([True , False , True]))

#print(ufo[ufo.City.isnull()])

#print(ufo[ufo.City.isnull()])

#print(ufo.dropna(how = 'all').shape)

#print(ufo.dropna(subset = ['City', 'Shape Reported'], how = 'all').shape)

#print(ufo['Shape Reported'].value_counts(dropna = False))

#ufo['Shape Reported'].fillna(value = "Various", inplace = True)

#print(ufo["Shape Reported"].value_counts())

