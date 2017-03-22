import pandas as pd 

ufo = pd.read_csv("http://bit.ly/uforeports")

#print(ufo.head(3))
#ilk satirin butun bilgilerini almis olduk.
#print(ufo.loc[0,:])
#0,1,2. sutuna ait butun bilgiler
#print(ufo.loc[[0,1,2],:])
#0 ve 2 dahil.
#ufo.loc[0:2,:]
#default olarak : geliyor.
#ufo.loc[0:2]

#print(ufo.loc[:,["City","State"]])

#City'den State'e kadar
#print(ufo.loc[:,"City":"State"])

#ufo[ufo.City == "Oakland"].State

#print(ufo.loc[ufo.City == "Oakland","State"])

#print(ufo.iloc[:,[0,3]])

#print(ufo.iloc[:,0:3])

#print(ufo.iloc[0:3 , :])

drinks = pd.read_csv("http://bit.ly/drinksbycountry",index_col = "country")

#print(drinks.ix["Albania",0])


#print(drinks.ix["Albania","beer_servings"])

#print(drinks.ix["Albania" : "Andorra",0:2])

#print(ufo.ix[0:2,0:2])