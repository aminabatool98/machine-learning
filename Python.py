import pandas as pd
import numpy as np 
import matplotlib.pyplot as py


df=pd.read_csv('dataset.csv')
print(df.head())

py.plot(df['CGPA'],df['Package_LPA'])