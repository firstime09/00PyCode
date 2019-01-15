import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({'H_Studied':[0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0],
                    'Test_Grade':[20, 21, 22, 23, 25, 37, 48, 56, 67, 76, 90, 89, 90]},
                    index=[0,1,2,3,4,5,6,7,8,9,10,11,12])
# print(df.describe())
dfX = df.H_Studied[:, np.newaxis]
dfY = df.Test_Grade.values

# dfX = df.H_Studied
# dfY = df.Test_Grade

clfLin = lm.LinearRegression()
clfLin.fit(dfX, dfY)
df['Test_Grade_Pred'] = clfLin.predict(dfX)

# Manually calculating R Squared
df['SST'] = np.square(df['Test_Grade'] - df['Test_Grade'].mean())
df['SSR'] = np.square(df['Test_Grade_Pred'] - df['Test_Grade'].mean())
RSquared = df['SSR'].sum() / df['SST'].sum()
print("SUM of SST: ", df['SST'].sum())
print("SUM of SSR: ", df['SSR'].sum())
print("R Squared: ", RSquared)

# for deg in [1, 2, 3, 4, 5]:
#     clfLin.fit(np.vander(dfX, deg + 1), dfY);
#     y_lr = clfLin.predict(np.vander(dfX, deg + 1))
#     plt.plot(dfX, y_lr, label='Degree' + str(deg));
#     plt.legend(loc=2);
#     # print()
# plt.plot(dfX, dfY, 'OK')

## plotting fitted line
plt.scatter(dfX, dfY, color='black')
plt.plot(dfX, df['Test_Grade_Pred'], color='blue', linewidth=3)
plt.title('Plotting Function')
plt.ylabel('Test_Grade')
plt.xlabel('H_Studied')
plt.show()
