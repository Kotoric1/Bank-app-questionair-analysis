# -*- coding: utf-8 -*-
#### Required Packages
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

data = pd.read_csv('C://Users//dell//Desktop//银行数据分析//data1.csv')
print (data)
dataset = pd.DataFrame(data)
######相关性分析
# X = dataset[:,1:98]
# y = dataset[:,0]
# cor = np.corrcoef(dataset,rowvar=0)[:]
######输出相关矩阵的第一列
# print (cor)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Correlation for Multicollinearity Check
corrMatrix = dataset.corr()

fig, ax = plt.subplots(figsize=(10, 8))
colormap = sns.diverging_palette(220, 10, as_cmap=True)
dropvals = np.zeros_like(corrMatrix)
dropvals[np.triu_indices_from(dropvals)] = True

sns.heatmap(corrMatrix, cmap=colormap, linewidths=0.5, annot=True, fmt='1.2f', mask=dropvals, vmin=-1, vmax=1)

plt.show()


# Variance Inflation Factor (VIF)
X = dataset[['学历','性别', '年龄','问题4','问题5', '问题6', '问题7', '问题8', '问题9', '问题10','问题11','问题12',
                                     '问题14', '问题15', '问题16', '问题17', '问题18','问题19']]

vif = pd.DataFrame()
vif["feature"] = X.columns

vif["VIF Factors"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

print(vif)

#######筛选后的数据读取
# data1 = pd.read_csv('data.csv')
X = dataset[['问题13','学历', '年龄', '问题7', '问题8', '问题9',
                                      '问题15', '问题16', '问题17', ]]
dataset1 = np.array(X)
######筛选后的变量######
X1 = dataset1[:,1:9]
Y1 = dataset1[:,0]
est = sm.OLS(Y1,X1).fit()
# est = sm.OLS(Y1, sm.add_constant(X1)).fit()
print (est.summary())
