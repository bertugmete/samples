#Open Source library for Data Analysis, Data manipulation , Data Visulation
#jupyter uzerinden tablo seklinde gorebiliriz.
import pandas as pd 
orders = pd.read_table("https://bitly.com/chiporders")

# birbirinden | ile ayrilmis olan datalari birlestirme
#Skip footer ve skiprows ile text'leri ayirabiliriz
user_cols = ['user_id','age','gender','occupation','zip_code']
users = pd.read_table("https://bitly.com/movieusers",sep='|',header=None, names =user_cols)
print(users.head())