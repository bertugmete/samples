import pandas as pd 

drinks = pd.read_csv("http://bit.ly/drinksbycountry")

#print(drinks.mean())
#Kıtalara gore beer_servings ortalamalari
#print(drinks.groupby('continent').beer_servings.mean())

#print(drinks.groupby('continent').beer_servings.max())


#Afrikadaki beer_servings ortalamasi
#print(drinks[drinks.continent == 'Africa'].beer_servings.mean())

#Beliri kategorilere gore listelemek icin

#print(drinks.groupby('continent').beer_servings.agg(['count','min','max','mean']))

#print(drinks.groupby('continent').mean())

print(drinks.groupby('continent').mean().plot(kind = 'bar'))