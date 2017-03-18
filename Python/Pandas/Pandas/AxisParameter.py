import pandas as pd 

drinks = pd.read_csv("http://bit.ly/drinksbycountry")

#print(drinks[drinks.country == "Turkey"])

#Continent kolonun silmek icin
#print(drinks.drop("continent",axis = 1).head())

#2. satirdaki veriyi silmek
#print(drinks.drop(2,axis = 0).head())

#ortalamayi verir.
#print(drinks.mean())

#satir bazinda ortalamayi alir.
#print(drinks.mean(axis= 1))

# axis = 0 yerine x = 'index' de kullanilabilir.

