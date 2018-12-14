import numpy as np
import pandas as pd
from sklearn.cros_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('C:/Users/user/Dropbox/MyDocument/Data Nitrogen - Lexi Pendong.xlsx')
print(df.head())
