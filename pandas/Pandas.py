import pandas as pd

df = pd.read_csv('customers-100.csv')

#print(df.head()) #mostrar las primeras filas

#print(df.isnull().sum()) #suma y muetras las celdas que no tengan datos

#df_cleaned = df.dropna() #elimina todas las filas que tengan un nulo

#filtrar
#chile_costumers =df[(df['Country']=='Chile') & (df['Company']=='Rasmussen Group')]
#print (chile_costumers)

#agregar nueva informacion
df['Subscription Date']= pd.to_datetime(df['Subscription Date'])
df['Days since Subscription']=(pd.Timestamp.now() - df['Subscription Date']).dt.days
#print (df.head)
#df.to_csv('newfile.csv',index=False)

customers_by_country=df.groupby('Country')['Customer Id'].count()
custom_sort= customers_by_country.sort_values(ascending=False)
print (custom_sort)