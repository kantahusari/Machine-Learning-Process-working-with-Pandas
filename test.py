import pandas as pd
import numpy as np

# 01
myDF=pd.read_csv('test.csv')

#02
myDF.head()

#03
myDF.columns=['ID','Range','Value','Machine Type','Zip code']
myDF

#04
myDF.style.set_caption('Kanta Husari 101217294')

#05
myDF.drop(['ID'], axis=1)

#06
myDF.dtypes

#07
myDF['Value']
myDF.Value
print("non of them ")

#08
myDF.Value.dtypes

#09
print(" Question 8: we can only apply this method myDF['Zip code'] because myDF.Zip code does not work because of the space andthe other column is Machine Type")

#10
myDF['Brand']=myDF['Machine Type']+' '+myDF['Zip code']
myDF['Brand']
myDF

#11
myDF['Total']=myDF['Range']*myDF['Value']
myDF

#12
myDF.head()
myDF.describe()
myDF.describe
myDF.shape
myDF.dtypes
print("Some of them are methods and some are attributes. Methods are callable. Anything that's callable, we need to use parenthesis.")
print("myDF.describe is the method itself but myDF.describe() calls the method, and returns the result.")

#13
myDF.describe(exclude=[np.number])

#14
myDF.rename(columns={'ID': 'My ID'})
myDF.head()

#15
myDF.rename(columns={'ID': 'My ID'}, inplace=True)
myDF.head()

#16
myDF.columns

#17
myDF.rename(columns={'My ID':'id', 'Range':'range', 'Value':'value', 'Machine Type':'machine type', 'Zip code':'zip code', 'Brand':'brand', 'Total':'total'}, inplace=True)
myDF.columns

#18
myDF.columns=myDF.columns.str.replace(' ', '_')
myDF.columns

#19
myDF.drop(['brand', 'total'], axis=1, inplace=True)
myDF

#20
myDF.drop(index=[3,5], inplace=True)
myDF.head()

#21
myDF.value.sort_values(ascending=True)

#22
myDF.sort_values('value',ascending =True)

# 23
myDF.sort_values('value',ascending =True,inplace =True)
myDF

#24
myDF.sort_values(['value','range'],ascending =[True,False])

#25
myDF[(myDF.range >=250)&(myDF.range<=350)]

# 26
myDF[(myDF.range >=250)&(myDF.range<=350)].sort_values(['range'],ascending =True)

#27
myDF[['id','value']][(myDF.range >=250)&(myDF.range<=350)]

#28
myDF[['id','value','machine_type']][(myDF.range >=250)&(myDF.range<=350) &( myDF.machine_type=='H')]

#29
myDF[( myDF.machine_type=='H') |( myDF.machine_type=='R')|( myDF.machine_type=='X')]

# 30
myDF.select_dtypes(include=[np.number])