# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:57:03 2020

@author: Amir Ranjouriheravi(71313)
"""

#Importing necessary data
import pandas as pd
df = pd.read_csv(r'https://raw.githubusercontent.com/carlson9/KocPython2020/master/homework/trend2.csv') 

#Importing necessary libraries
import numpy as np
import pystan
from sklearn import preprocessing
import matplotlib.pyplot as plt

#Preparing data
df = df.drop('cc', axis=1)
df = df.dropna()
df = df.reset_index().drop('index', axis=1)
unique_country = df.loc[: , 'country'].str.strip().unique()
unique_year = np.unique(df.loc[: , 'year'])
num_country = len(unique_country)
num_year = len(unique_year)
#print(num_country, num_year)
church = df.loc[: , 'church2'].values
gini = df.loc[: , 'gini_net'].values
gdp = df.loc[: , 'rgdpl'].values
le = preprocessing.LabelEncoder()
df['country_code'] = le.fit_transform(df['country']) 
c_code = df['country_code'].values
country_lookup = dict(zip(unique_country, range(num_country)))
df['year_code'] = le.fit_transform(df['year']) 
y_code = df['year_code'].values
year_lookup = dict(zip(unique_year, range(num_year)))
#print(year_lookup)

#Distribution of Gini index
#df.gini_net.hist(bins=25)
#plt.title('Distribution of Gini index')
#plt.xlabel('Gini index')
#plt.ylabel('Frequency')

#Informative prior for b1 (with country)
varying_intercept1 = """
data {
    int<lower=0> N; 
    int<lower=0> J; 
    int<lower=1,upper=J> country[N]; 
    vector[N] gini_expl;
    vector[N] gdp_cont;
    vector[N] relig_out;
}
parameters {
    vector[J] a;
    real b1;
    real b2;
    real mu_a;
    real<lower=0,upper=100> sig_a;
    real<lower=0,upper=100> sig_y;
}
transformed parameters {
    vector[N] y_hat;
    
    for (i in 1:N) 
      y_hat[i] = a[country[i]] + gini_expl[i] * b1 + gdp_cont[i] * b2;
  
}
model {
    sig_a ~ uniform(0, 1);
    a ~ normal (mu_a, sig_a);
    b1 ~ normal (0, 100);
    b2 ~ normal (0, 1);
    sig_y ~ uniform(0, 1);
    relig_out ~ normal(y_hat, sig_y);
}
"""

varying_intercept_data1 = {'N': len(church),
                'J': len(unique_country),
                'country': c_code +1,
                'gini_expl': gini,
                'gdp_cont': gdp,
                'relig_out': church}

sm1 = pystan.StanModel(model_code=varying_intercept1)
varying_intercept_fit1 = sm1.sampling(data=varying_intercept_data1, iter=200, chains=2)

#other models' code are same with the first one except changing prior distributions for b1 and using year.

#Uninformative prior for b1 (with country)
varying_intercept2 = """
data {
    int<lower=0> N; 
    int<lower=0> J; 
    int<lower=1,upper=J> country[N]; 
    vector[N] gini_expl;
    vector[N] gdp_cont;
    vector[N] relig_out;
}
parameters {
    vector[J] a;
    real b1;
    real b2;
    real mu_a;
    real<lower=0,upper=100> sig_a;
    real<lower=0,upper=100> sig_y;
}
transformed parameters {
    vector[N] y_hat;
    
    for (i in 1:N) 
      y_hat[i] = a[country[i]] + gini_expl[i] * b1 + gdp_cont[i] * b2;
  
}
model {
    sig_a ~ uniform(0, 1);
    a ~ normal (mu_a, sig_a);
    b1 ~ normal (0, 1);
    b2 ~ normal (0, 1);
    sig_y ~ uniform(0, 1);
    relig_out ~ normal(y_hat, sig_y);
}
"""

varying_intercept_data2 = {'N': len(church),
                'J': len(unique_country),
                'country': c_code +1,
                'gini_expl': gini,
                'gdp_cont': gdp,
                'relig_out': church}

sm2 = pystan.StanModel(model_code=varying_intercept2)
varying_intercept_fit2 = sm2.sampling(data=varying_intercept_data2, iter=200, chains=2)

#Informative prior for b1 (with year)
varying_intercept3 = """
data {
    int<lower=0> N; 
    int<lower=0> J; 
    int<lower=1,upper=J> year[N]; 
    vector[N] gini_expl;
    vector[N] gdp_cont;
    vector[N] relig_out;
}
parameters {
    vector[J] a;
    real b1;
    real b2;
    real mu_a;
    real<lower=0,upper=100> sig_a;
    real<lower=0,upper=100> sig_y;
}
transformed parameters {
    vector[N] y_hat;
    
    for (i in 1:N) 
      y_hat[i] = a[year[i]] + gini_expl[i] * b1 + gdp_cont[i] * b2;
  
}
model {
    sig_a ~ uniform(0, 1);
    a ~ normal (mu_a, sig_a);
    b1 ~ normal (0, 100);
    b2 ~ normal (0, 1);
    sig_y ~ uniform(0, 1);
    relig_out ~ normal(y_hat, sig_y);
}
"""

varying_intercept_data3 = {'N': len(church),
                'J': len(unique_year),
                'year': y_code+1,
                'gini_expl': gini,
                'gdp_cont': gdp,
                'relig_out': church}

#model_fit = pystan.stan(model_code=varying_intercept, data=varying_intercept_data, iter=1000, chains=2)
sm3 = pystan.StanModel(model_code=varying_intercept3)
varying_intercept_fit3 = sm3.sampling(data=varying_intercept_data3, iter=200, chains=2)

#Uninformative prior for b1 (with year)
varying_intercept4 = """
data {
    int<lower=0> N; 
    int<lower=0> J; 
    int<lower=1,upper=J> year[N]; 
    vector[N] gini_expl;
    vector[N] gdp_cont;
    vector[N] relig_out;
}
parameters {
    vector[J] a;
    real b1;
    real b2;
    real mu_a;
    real<lower=0,upper=100> sig_a;
    real<lower=0,upper=100> sig_y;
}
transformed parameters {
    vector[N] y_hat;
    
    for (i in 1:N) 
      y_hat[i] = a[year[i]] + gini_expl[i] * b1 + gdp_cont[i] * b2;
  
}
model {
    sig_a ~ uniform(0, 1);
    a ~ normal (mu_a, sig_a);
    b1 ~ normal (0, 1);
    b2 ~ normal (0, 1);
    sig_y ~ uniform(0, 1);
    relig_out ~ normal(y_hat, sig_y);
}
"""

varying_intercept_data4 = {'N': len(church),
                'J': len(unique_year),
                'year': y_code + 1,
                'gini_expl': gini,
                'gdp_cont': gdp,
                'relig_out': church}

#model_fit = pystan.stan(model_code=varying_intercept, data=varying_intercept_data, iter=1000, chains=2)
sm4 = pystan.StanModel(model_code=varying_intercept4)
varying_intercept_fit4 = sm4.sampling(data=varying_intercept_data4, iter=200, chains=2)

#comments
#First of all, let me convey my sincere gratitude to you for letting me get deepeer in the pystan library
#More days gave me the chance to review the resources of the pystan. As I am relatively new to the 
#python I really want to learn every site_package along with its details.Although I managed to excute my 
#pystan model without varying intercept, because of the hard work load my old computer hanged up. That is 
#why I have not conclude it with the last due comment.











  

