# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:29:42 2020

@author: Amir Ranjouriheravi(71313)
"""



import numpy as np
import pandas as pd
from scipy.stats import t


def ols_reg(filename, target, covariates, alpha = 0.025, exxcel=0):
    
    if exxcel == 1:
        df = pd.read_excel(f"{filename}.xlsx")  #It has been assumed that the file is in the same directory with your python process is based. 
    else:
        pass
    
    if exxcel == 0:
        sepp = input('what is your csv file sepration method(, or ;)-> sep:')    
        df = pd.read_csv(f"{filename}.csv", sep= f'{sepp}')     #It has been assumed that the file is in the same directory with your python process is based.   
    else:
        pass
    
    df_1 = df.apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()
    a = df_1[[f'{target}']].values
    am = df_1[covariates].values
    (d,c) = np.shape(am)
    ami = np.c_[np.ones(d), am]
    amir = ami.transpose()
    amirr = np.dot(amir, ami)
    amirra = np.linalg.inv(amirr)
    amirran = np.dot(amirra, amir)
    amirranj = np.dot(amirran, a)
    (m,n) = np.shape(amirranj)
    index = []
    for i in range(m):
        x = 'b'+'_'+ (f'{i}')
        index.append(x)
    beta = pd.DataFrame(amirranj, index = index, columns = ['Estimated Parameters'])
    B = []
    for i in range(m):
        B.append(float(beta.iloc[i]))    
    
    if len(covariates) == 1:
        df_1[f'Estimated {target}'] = B[0] + df_1[covariates[0]] * B[1]
    else:
        pass
    
    if len(covariates) == 2:    
        df_1[f'Estimated {target}'] = B[0] + df_1[covariates[0]] * B[1] + df_1[covariates[1]] * B[2]
    else:
        pass
    
    if len(covariates) == 3:    
        df_1[f'Estimated {target}'] = B[0] + df_1[covariates[0]] * B[1] + df_1[covariates[1]] * B[2] + df_1[covariates[2]] * B[3]     
    else:
        pass
    
    if len(covariates) == 4:    
        df_1[f'Estimated {target}'] = B[0] + df_1[covariates[0]] * B[1] + df_1[covariates[1]] * B[2] + df_1[covariates[2]] * B[3] + df_1[covariates[3]] * B[4]    
    else:
        pass 
    
    if len(covariates) == 5:    
        df_1[f'Estimated {target}'] = B[0] + df_1[covariates[0]] * B[1] + df_1[covariates[1]] * B[2] + df_1[covariates[2]] * B[3] + df_1[covariates[3]] * B[4] + df_1[covariates[4]] * B[5]    
    else:
        pass
    
    df_1['Error'] = df_1[f'{target}'] - df_1[f'Estimated {target}']
    print('You are observing the first five rows of your data frame after estimation:')
    print(df_1.head())
    
    le = len(covariates)
    e = df_1[['Error']].values
    e_trans = e.transpose()
    ee = np.dot(e_trans, e)
    fd = d - (le + 1)
    var_ee = float(ee / fd)
    var_cov = var_ee * amirra
    var_cov_pd = pd.DataFrame(var_cov, index = index, columns = index)
    varrr = []
    for i in range(le + 1):
        varrr.append(var_cov[i,i])
    print()
    print('Variance_Covariance matrix is equal to :\n ' , var_cov_pd)
    
    
    se = pd.Series(varrr)
    beta['Est variances'] = se.values    
    cvvv = [item**(0.5) for item in varrr]
    t_test = t.ppf(1 - alpha, df = fd)
    distance = []
    for i in range(len(cvvv)):
        fff = t_test * cvvv[i]
        distance.append(fff)
    distance_ser = pd.Series(distance)
    
    beta['interval start'] = pd.Series(beta['Estimated Parameters']).values - distance_ser.values
    beta['interval end'] = pd.Series(beta['Estimated Parameters']).values + distance_ser.values
    print()
    print(beta)
    
    
#ols_reg('test', 'consume', ['income', 'wealth'])
#ols_reg('winequality-white', 'fixed acidity', ['citric acid', 'free sulfur dioxide', 'residual sugar'])




