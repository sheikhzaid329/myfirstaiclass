import pandas as pd

df=pd.read_csv('Numpy Pandas Practice/RealEstate-USA.csv',delimiter=',')

print(df)

status=df['status']

print(status)

print(df.tail(3))

print(df.head(3))

print(df.shape)

print(df.loc[:5,['status','street']])

