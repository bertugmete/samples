import pandas as pd 

drinks = pd.read_csv("http://bit.ly/drinksbycountry")

#print(drinks.loc[23, 'beer_servings'])

#print(drinks.loc['Brazil', 'beer_servings'])

#print(drinks.index.name == None)

#drinks.index.name = 'country'

#drinks.reset_index(inplace = True)

#print(drinks.head())

#print(drinks.describe())

#print(drinks.describe().columns)

#print(drinks.describe().loc['25%' , 'beer_servings'])

drinks.set_index("country",inplace=True)

#print(drinks.head())

#print(drinks.continent.head())

#print(drinks.continent.value_counts())
#print(drinks.continent.value_counts()["Africa"])

#print(drinks.continent.value_counts().sort_index())

people = pd.Series([300000,85000], index = ["Albania","Andorra"], name = "population")

#print(people)

#print(drinks.beer_servings * people)

print(pd.concat([drinks, people], axis = 1).head())