import pandas as pd

data = pd.read_csv("C://Users//dell//Desktop//银行数据分析//data.csv")
test = pd.read_csv("C://Users//dell//Desktop//银行数据分析//test.csv")
y = data['问题20']

X = data.drop(['问题20'], axis=1)
X = X.fillna(0.0).astype(int)
X_test = test


# 导入k近邻模型的类
from sklearn.neighbors import KNeighborsClassifier
# 构建k近邻模型
kn = KNeighborsClassifier()
kn.fit(X, y)
print(kn)

# 预测测试集
kn_pred = kn.predict(X_test)
print(kn_pred)

# 模型得分
print('k临近模型在训练原始数据集上的准确率%f' %kn.score(X,y))

# 导入GBDT模型的类
from sklearn.ensemble import GradientBoostingClassifier
# 构建GBDT模型
gbdt = GradientBoostingClassifier()
gbdt.fit(X, y)
print(gbdt)

# 预测测试集
gbdt_pred = gbdt.predict(X_test)
print(gbdt_pred)

# 模型得分
print('GBDT模型在训练集上的准确率%f' %gbdt.score(X,y))

