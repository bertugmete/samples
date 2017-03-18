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

