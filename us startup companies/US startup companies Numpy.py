import numpy as np
Valuation, Date_joined,Industries, select_Investers= np.genfromtxt('us startup companies/Startups in 2021 end.csv',delimiter=',', usecols=[2,3,5,6],unpack=True,dtype=None,skip_header=1)

print(Valuation)
print(Date_joined)
print(Industries)
print(select_Investers)

dimension=np.array([Industries,     
           select_Investers])

print('Number of Dimensions :', dimension.ndim)