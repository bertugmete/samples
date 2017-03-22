import pandas as pd

ufo = pd.read_csv("http://bit.ly/uforeports")

#print(ufo.drop("City",axis = 1).head())

#ufo.drop("City",axis = 1,inplace = True)

#print(ufo.head())

#print(ufo.dropna(how = "any").shape)

ufo = ufo.set_index("Time",inplace = True)

#print(ufo.tail())

#print(ufo.fillna(method = "fill").tail())