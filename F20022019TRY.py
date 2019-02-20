import numpy as np
import pandas as pd

dframe = pd.read_excel('D:/00RCode/Result/580_CIDANAU_190219N.xlsx')
target = 'New2_B7'
loadDT = np.asarray(dframe[target])
print(loadDT)

mean = loadDT.mean()
std = loadDT.std()
sigma = std**2

print(mean, std, sigma)
