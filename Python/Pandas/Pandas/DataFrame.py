import pandas as pd 
#read_csv aralarinda ',' olanlari okumakta daha iyidir.
#ufo = pd.read_csv("https://bit.ly/uforeports",sep=',')

#print(ufo.head())
#buyuk ve kucuk harf duyarliligi var.
#print(ufo['City'])
#print(ufo.City)
#Kolon basliklarinda bosluk varsa '_' ile yazamayiz o yuzden [] arasina string ifade seklinde yazmaliyiz.
#print(ufo['Colors Reported'])

#Iki kolonu birlestirerek tek kolon haline getirdik.
#ufo["Location"] = ufo.City + "," +  ufo.State

#print(ufo.head())

#movies = pd.read_csv("https://bit.ly/imdbratings")
#print(movies)
#istatiksel olarak cikarir
#print(movies.describe())

#print(movies.describe(include=['object']))
#Kolon isimlerini degistirme
#ufo = pd.read_csv("https://bit.ly/uforeports")
#ufo.rename(columns={"Colors Reported" : "Colors_Reported","Shape Reported":"Shape_Reported"})

# cok sayidaki kolon adini degistirmek icin
#ufo.columns = ufo.columns.str.replace(' ','_')

#print(ufo.head())

#Remove Colums From DataFrame

#ufo = pd.read_csv("https://bit.ly/uforeports")

#ufo.drop("Colors Reported",axis=1,inplace= True)

#print(ufo.head())

# tek seferde birden fazla kolon silme
#ufo.drop(['City','State'],axis=1,inplace=True)
#ilk satirda bulunan veriyi silmis olduk.
#ufo.drop([0,1] , axis=0 , inplace=True ) 

#print(ufo.head())

#Sort Datas

#movies = pd.read_csv("https://bit.ly/imdbratings")

#print(movies.title.sort_values())

#print(movies['title'].sort_values())

#print(movies.title.sort_values(ascending=False))

#print(movies.sort_values(["content_rating","duration"]))

#Filter