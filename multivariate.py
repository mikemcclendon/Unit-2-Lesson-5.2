import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('LoanStats3a.csv', skiprows=1)
loansData2 = loansData[['annual_inc', 'int_rate', 'home_ownership']]
ld = loansData2.dropna(subset = ['annual_inc', 'int_rate', 'home_ownership'])
#creating subset, dropping na

ld['hodummy'] = map(lambda x: 1 if x == 'OWN' else 0, ld['home_ownership']) 
#I interpreted the question to indicate that only whether someone was a homeowner was of interest
ld['cleanintrate'] = map(lambda x: str(x)[:-1], ld['int_rate'])
ld['cleanintratenum'] = ld[['cleanintrate']].convert_objects(convert_numeric=True) #says is deprecated, but to_numeric doesn't work
cleanintrate = map(lambda x: x/100, ld['cleanintratenum'])
ld['int_rate'] = cleanintrate
#cleaning interest rate

def main():

	X = ld[['annual_inc']]
	y = ld['int_rate']
	X = sm.add_constant(X)
	est = sm.OLS(y, X).fit()
	print(est.summary())
	#modeling int_rate using income

	X1 = ld[['annual_inc', 'hodummy']]
	y1 = ld['int_rate']
	X1 = sm.add_constant(X1)
	est1 = sm.OLS(y1, X1).fit()
	print(est1.summary())
	#modeling int_rate using income and homeownership

if __name__ == "__main__":
    main()














