# coding: utf-8
import csv

from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import pygal

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv("C://Users//dell//Desktop//银行数据分析//K-means.csv")
# data = data.fillna(0.0).astype(int)

y1 = data['性别']
y2 = data['年龄']
y3 = data['学历']
y = pd.concat([y1, y2, y3], axis=1)

X1 = data.drop(['问题20'], axis=1)
X2 = X1.drop(['性别'], axis=1)
X3 = X2.drop(['年龄'], axis=1)
X = X3.drop(['学历'], axis=1)

SSE = []

for i in range(1, 20):
    k_means = KMeans(n_clusters=i)
    k_means.fit(X)
    SSE.append(k_means.inertia_)

plt.plot(range(1, 20), SSE, marker='o')
plt.xlabel('聚类组数')
plt.ylabel('误差平方和')
plt.show()

# n_cluster = 4
k_model = KMeans(n_clusters=4)
k_model.fit(X)

label = pd.Series(k_model.labels_)
num = pd.Series(k_model.labels_).value_counts()
# print(num)
center = pd.DataFrame(k_model.cluster_centers_)
# print(center)
r = pd.concat([center, num], axis=1)
# print(r)
r.columns = list(X.columns) + ['类别数目']
# print(r)

# 使用ggplot的绘图风格
plt.style.use('ggplot')

N = len(k_model.cluster_centers_[0])
angles = np.linspace(0, 2*np.pi, N, endpoint=False) # 设置雷达图的角度，用于平分切开一个圆面
angles = np.concatenate((angles, [angles[0]])) # 为了使雷达图一圈封闭起来
fig = plt.figure(figsize=(7,7)) # 设置画布大小
ax = fig.add_subplot(111, polar=True) # 这里一定要设置为极坐标格式
sam = ['r-', 'o-', 'g-', 'b-', 'p-'] # 样式
lab = [] # 图例标签名
for i in range(len(k_model.cluster_centers_)):
    values = k_model.cluster_centers_[i]
    feature = ['问题4','问题5','问题6','问题7','问题8', '问题9','问题10','问题11','问题12',
               '问题13','问题14','问题15','问题16','问题17','问题18','问题19'] # 设置各指标名称
    # 为了使雷达图一圈封闭起来，需要下面的步骤
    values=np.concatenate((values,[values[0]]))
    ax.plot(angles, values, sam[i], linewidth=2) # 绘制折线图
    ax.fill(angles, values, alpha=0.25) # 填充颜色
    ax.set_thetagrids(angles[:-1] * 180/np.pi, feature) # 添加每个特征的标签

    ax.set_ylim(-5, 5) # 设置雷达图的范围
    plt.title('客户群特征分布图') # 添加标题
    ax.grid(True) # 添加网格线
    j = i + 1
    lab.append('客户群'+str(j))
plt.legend(lab)
plt.show()

xy = pd.concat([X, y], axis=1)
res = pd.concat([xy,pd.Series(k_model.labels_, index=X.index)],axis=1)  # 详细输出每个样本对应的类别
res.columns = list(xy.columns) + ['类别'] # 重命名表头


types_df = res[['性别', '年龄', '学历', '类别']]


class_0 = types_df[types_df.类别.isin([0])]
class_0 = class_0.drop(['类别'], axis=1)

class_1 = types_df[types_df.类别.isin([1])]
class_1 = class_1.drop(['类别'], axis=1)

class_2 = types_df[types_df.类别.isin([2])]
class_2 = class_2.drop(['类别'], axis=1)

class_3 = types_df[types_df.类别.isin([3])]
class_3 = class_3.drop(['类别'], axis=1)


k_model_0 = KMeans(n_clusters=1)
k_model_0.fit(class_0)

num_0 = pd.Series(k_model_0.labels_).value_counts()
# print(num)
center_0 = pd.DataFrame(k_model_0.cluster_centers_)

k_model_1 = KMeans(n_clusters=1)
k_model_1.fit(class_1)

num_1 = pd.Series(k_model_1.labels_).value_counts()
# print(num)
center_1 = pd.DataFrame(k_model_1.cluster_centers_)


k_model_2 = KMeans(n_clusters=1)
k_model_2.fit(class_2)

num_2 = pd.Series(k_model_2.labels_).value_counts()
# print(num)
center_2 = pd.DataFrame(k_model_2.cluster_centers_)


k_model_3 = KMeans(n_clusters=1)
k_model_3.fit(class_3)

num_3 = pd.Series(k_model_3.labels_).value_counts()
# print(num)
center_3 = pd.DataFrame(k_model_3.cluster_centers_)


r_end = pd.concat([center_0, center_1, center_2, center_3], axis=0)

list_0 = r_end.iloc[0].tolist()
list_1 = r_end.iloc[1].tolist()
list_2 = r_end.iloc[2].tolist()
list_3 = r_end.iloc[3].tolist()


# 导入第三方模块
import numpy as np
import matplotlib.pyplot as plt

# 构造数据
values = list_0
values1 = list_1
values2 = list_2
values3 = list_3
feature = ['性别','年龄','学历']

N = len(values)
# 设置雷达图的角度，用于平分切开一个圆面
angles=np.linspace(0, 2*np.pi, N, endpoint=False)
# 为了使雷达图一圈封闭起来，需要下面的步骤
values=np.concatenate((values,[values[0]]))
values1=np.concatenate((values1,[values1[0]]))
values2=np.concatenate((values2,[values2[0]]))
values3=np.concatenate((values3,[values3[0]]))

angles=np.concatenate((angles,[angles[0]]))

# 绘图
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)
# 绘制折线图
ax.plot(angles, values, '', linewidth=1, label = '客户群1')
# 填充颜色
ax.fill(angles, values, alpha=0.25)
# 绘制第二条折线图
ax.plot(angles, values1, '', linewidth=1, label = '客户群2')
ax.fill(angles, values1, alpha=0.25)

# 绘制第三条折线图
ax.plot(angles, values2, '', linewidth=1, label = '客户群3')
ax.fill(angles, values2, alpha=0.25)

# 绘制第四条折线图
ax.plot(angles, values3, '', linewidth=1, label = '客户群4')
ax.fill(angles, values3, alpha=0.25)

# 添加每个特征的标签
ax.set_thetagrids(angles[:-1] * 180/np.pi, feature)
# 设置雷达图的范围
ax.set_ylim(0,5)
# 添加标题
plt.title('客户群特征分布图')

# 添加网格线
ax.grid(True)
# 设置图例
plt.legend(loc = 'best')
# 显示图形
plt.show()

