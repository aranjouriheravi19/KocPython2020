# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 02:12:27 2020

@author: dmin
"""

from urllib.request import urlretrieve
from ols_reg_function import *


# Import pandas
import pandas as pd

# Assign url of file: url
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

# Save file locally
urlretrieve(url, 'winequality-white.csv')

# Run our written function
ols_reg('winequality-white', 'fixed acidity', ['citric acid', 'free sulfur dioxide', 'residual sugar'])