import pandas as pd

movies = pd.read_csv("http://bit.ly/imdbratings")

booleans = []

#for length in movies.duration:
#    if length  >= 200:
#        booleans.append("true")
#    else :
#        booleans.append("false")

#print(len(booleans))


#is_long = pd.Series(booleans)

#print(is_long.head())

#print(movies[is_long])

#is_long = movies.duration >= 200
#print(is_long.head())

#print(movies[movies.duration >= 200])

#print(movies[movies.duration >= 200]['genre'])

#MULTIPLE FILTER IN PANDAS
#print(movies[(movies.duration >= 200) & (movies.genre == "Drama")])

#print(movies[(movies.duration >= 200) | (movies.genre == "Drama")])

#puani 7 den yuksek ve komedi filmleri getirdik.
#print(movies[(movies.star_rating >= 7) & (movies.genre == "Comedy")],movies.title, movies.star_rating)

#print(movies[movies.genre.isin(['Crime','Comedy','Action'])])