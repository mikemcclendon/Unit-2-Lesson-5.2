import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('LoanStats3a.csv', skiprows=1)

loansData['hodummy'] = map(lambda x: 0 if x == 'RENT' else 1, loansData['home_ownership'])
loansData['cleanintrate'] = map(lambda x: str(x)[:-1], loansData['int_rate'])
loansData['cleanintratenum'] = loansData[['cleanintrate']].convert_objects(convert_numeric=True) #says is deprecated, but to_numeric doesn't work
cleanintrate = map(lambda x: x/100, loansData['cleanintratenum'])
loansData['int_rate'] = cleanintrate
ld = loansData.dropna(subset = ['annual_inc', 'int_rate', 'hodummy'])
#cleaning, dropping nulls, and converting data to dummies



X = ld[['annual_inc' , 'hodummy']]
y = ld['int_rate']
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()
#est1 = sm.OLS(formula='int_rate ~ annual_inc : home_ownership', data = ld).fit()
print(est.summary())
#print est1.params, '\n'
#print est2.params














