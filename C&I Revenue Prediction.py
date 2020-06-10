# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:21:05 2019

@author: Ashish.Gupta
"""

import pandas as pd

df = pd.read_excel('D:\Personal\Machine Learning\Income Statement Dashboard 2019 Apr 1.0.xlsx',sheet_name='CI')

#print(df.columns)

X = df.iloc[:, 3:12].values
#print (X.shape)

Y = df.iloc[:, 13].values
    

#Split data using Train and Test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

#Multiple Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
#Train Model
model.fit(X_train, y_train)
#model.coef_    
print(model.score(X_test, y_test))



#from sklearn.linear_model import LogisticRegression
#logmodel = LogisticRegression()
#logmodel.fit(X_train, y_train)
#predictions = logmodel.predict(X_test)