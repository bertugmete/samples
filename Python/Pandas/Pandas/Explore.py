import pandas as pd 

movies = pd.read_csv("http://bit.ly/imdbratings")


#toplamini unique sayisini, top olani ve frequence gosterir.
#print(movies.genre.describe())

#belirli bir kategoriye ait olanlarin sayisini getirir.
#print(movies.genre.value_counts())

#belirli bir kategoriye ait olanlarin toplamdaki oranini gosterir.

#print(movies.genre.value_counts(normalize = True))

#print(movies.genre.unique())

#print(pd.crosstab(movies.genre , movies.content_rating))

#print(movies.duration.describe())

#int iceren datalar icin kullanisli
#print(movies.duration.value_counts())

#%matplotlib inline 
#histogram grafik cizdirmek icin
#print(movies.duration.plot(kind = 'hist'))

print(movies.genre.value_counts())