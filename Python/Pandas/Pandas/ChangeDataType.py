import pandas as pd

drinks = pd.read_csv("http://bit.ly/drinksbycountry")

#print(drinks.dtypes)

#kolonun data tipini degistirdik.
drinks["beer_servings"] = drinks.beer_servings.astype(float)

#print(drinks.dtypes)

#drinks = pd.read_csv("http://bit.ly/drinksbycountry",dtype={'beer_servings:' : float})

orders = pd.read_table("http://bit.ly/chiporders")

