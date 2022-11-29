#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import pickle
import pandas as pd
#mat plot
import numpy as np
#Sk learn imports
from sklearn import tree,preprocessing
#ensembles
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier
import sklearn.metrics as metrics
#scores
from sklearn.metrics import confusion_matrix,accuracy_score,roc_curve,roc_auc_score,auc  
#models
from sklearn.model_selection import StratifiedKFold,train_test_split,cross_val_score,learning_curve,GridSearchCV,validation_curve
from sklearn import tree,preprocessing

from sklearn.preprocessing import StandardScaler

df = pd.read_csv(r"C:\HACKATHON_MODEL\Life Expectancy Data_HV22.csv")


# In[23]:


# Replacing the Null Values with mean values of the data
from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=np.nan,strategy='mean',fill_value=None)

df['Life expectancy ']=imputer.fit_transform(df[['Life expectancy ']])
df['Adult Mortality']=imputer.fit_transform(df[['Adult Mortality']])
df['Alcohol']=imputer.fit_transform(df[['Alcohol']])
df['Hepatitis B']=imputer.fit_transform(df[['Hepatitis B']])
df[' BMI ']=imputer.fit_transform(df[[' BMI ']])
df['Polio']=imputer.fit_transform(df[['Polio']])
df['Total expenditure']=imputer.fit_transform(df[['Total expenditure']])
df['Diphtheria ']=imputer.fit_transform(df[['Diphtheria ']])
df['GDP']=imputer.fit_transform(df[['GDP']])
df['Population']=imputer.fit_transform(df[['Population']])
df[' thinness  1-19 years']=imputer.fit_transform(df[[' thinness  1-19 years']])
df[' thinness 5-9 years']=imputer.fit_transform(df[[' thinness 5-9 years']])
df['Income composition of resources']=imputer.fit_transform(df[['Income composition of resources']])
df['Schooling']=imputer.fit_transform(df[['Schooling']])


# In[24]:


df.describe(include="all")


# In[25]:


df.corr()["Life expectancy "].sort_values(ascending=False)[1:]


# In[26]:


lst=['Schooling','Income composition of resources',' BMI ','Diphtheria ','Polio','under-five deaths ',' thinness 5-9 years',' thinness  1-19 years',' HIV/AIDS','Adult Mortality','Life expectancy ']                   


# In[27]:


df2=df[lst]
df2


# In[28]:


#splitting into target and predictor values
y=df2[["Life expectancy "]]


# In[29]:


df2.drop(["Life expectancy "],axis=1,inplace=True)


# In[30]:


# define standard scaler
scaler = StandardScaler()
# transform data
scaled = scaler.fit_transform(df2)
df = pd.DataFrame(scaled,columns=df2.columns)


# In[31]:


x=df


# In[32]:


x


# In[33]:


from sklearn.model_selection import train_test_split

# Splitting the data into train and test (0.75/0.25 train/test). Shuffle the data

features_train, features_test, targets_train, targets_test = train_test_split(x, y, shuffle=True)


# In[34]:


from sklearn.ensemble import RandomForestRegressor

# Creating a random forest regressor with 100 trees and fitting it to our data

forest = RandomForestRegressor(n_estimators=100)
model=forest.fit(features_train, targets_train)


# In[35]:


pickle.dump(model, open('life.pkl', 'wb'))


# In[ ]:




