#print('merhaba'.upper())

import pandas as pd

orders = pd.read_table("http://bit.ly/chiporders")

#print(orders.head())

#buyuk harfle yazdirmak icin
#print(orders.item_name.str.upper())

#print(orders.item_name.str.contains('Chicken').head())

#ayni anda birden fazla replace yapilabilir.
orders.choice_description.str.replace(']','').str.replace(']','')

print(orders)