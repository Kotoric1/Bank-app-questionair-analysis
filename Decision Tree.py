

import numpy as np
import matplotlib.pyplot as plt
import os
import xlrd
import pandas as pd
from pymongo import MongoClient
import statsmodels.api as sm

male=0
female=0
none=0
false=0
total_number=0
path="C://Users//dell//Desktop//银行数据分析//原始数据与要求//原始数据集"
upath=path.encode('utf-8').decode('utf-8')
dirs=os.listdir(upath)
client = MongoClient('localhost', 27017)

for file in dirs:
    if file.endswith('.xls') or file.endswith('.et'):
        excel=pd.ExcelFile(os.path.join(upath,file))
        book=xlrd.open_workbook(excel)
        #print(f"包含表单数量 {book.nsheets}")
        #print(f"表单的名分别为: {book.sheet_names()}")
        i=0

        #print(count)
        for i in range(book.nsheets):
                sheet = book.sheet_by_index(i)
                #print(f"表单索引：{sheet.number}")
                #print(f"表单行数：{sheet.nrows}")
                #print(f"表单列数：{sheet.ncols}")
                total_number=total_number+1
                if sheet.nrows==0 and sheet.ncols==0:
                    break
                else:
                    count = 0
                    myDict={}
                    #print(f"表单名：{sheet.name}")
                    myDict['姓名']=sheet.name
                    #第一题
                    if sheet.cell(3,0).ctype==1:
                        if sheet.cell(4, 0).ctype == 1:
                            #print(f"性别：单选题多选")
                            myDict['性别']=4
                            false=false+1
                        else:
                            male=male+1
                            #print('性别：男')
                            myDict['性别']=1
                    else:
                        if sheet.cell(4,0).ctype==0:
                            #print(f"性别：未填写")
                            none=none+1
                            myDict['性别']=3
                        else:
                            #print(f"性别：女")
                            female = female + 1
                            myDict['性别']=2
                    #第二题
                    list1=[sheet.cell(6,0).ctype,sheet.cell(7,0).ctype,sheet.cell(8,0).ctype,sheet.cell(9,0).ctype,sheet.cell(10,0).ctype,sheet.cell(11,0).ctype]
                    if list1.count(1)>1:
                        myDict['年龄'] = 6
                    elif list1.count(1)==0:
                        myDict['年龄'] = 7
                    else:
                        index = list1.index(1)
                        myDict['年龄'] = index
                    list1.clear()

                    #第三题
                    list1=[sheet.cell(13,0).ctype,sheet.cell(14,0).ctype,sheet.cell(15, 0).ctype]
                    if list1.count(1) > 1:
                        myDict['学历'] = 3
                    elif list1.count(1) == 0:
                        myDict['学历'] = 4
                    else:
                        index = list1.index(1)
                        myDict['学历'] = index
                    list1.clear()

                    # 第四题
                    list1 = [sheet.cell(17, 0).ctype, sheet.cell(18, 0).ctype, sheet.cell(19, 0).ctype]
                    if list1.count(1) > 1:
                        myDict['问题4'] = 0
                    elif list1.count(1) == 0:
                        myDict['问题4'] = 0
                    else:
                        index = list1.index(1)
                        myDict['问题4'] = index+1
                    list1.clear()

                    # 第五题
                    list1 = [sheet.cell(21, 0).ctype, sheet.cell(22, 0).ctype, sheet.cell(23, 0).ctype]
                    if list1.count(1) > 1:
                        myDict['问题5'] = 0
                    elif list1.count(1) == 0:
                        myDict['问题5'] = 0
                    else:
                        index = list1.index(1)
                        myDict['问题5'] = index+1
                    list1.clear()

                    # 第六题
                    list1 = [sheet.cell(25, 0).ctype, sheet.cell(26, 0).ctype, sheet.cell(27, 0).ctype,
                            sheet.cell(28, 0).ctype]
                    if list1.count(1) == 1 and list1.index(1) == 1:
                        myDict['问题6'] = 1
                        count=count+1
                    else:
                        myDict['问题6'] = 0
                    list1.clear()

                    # 第七题
                    list1 = [sheet.cell(30, 0).ctype, sheet.cell(31, 0).ctype, sheet.cell(32, 0).ctype,
                            sheet.cell(33, 0).ctype, sheet.cell(34, 0).ctype]
                    if list1.count(1) == 1 and list1.index(1) == 1:
                        myDict['问题7'] = 1
                        count=count+1
                    else:
                        myDict['问题7'] = 0
                    list1.clear()

                    # 第八题
                    list1 = [sheet.cell(36, 0).ctype, sheet.cell(37, 0).ctype, sheet.cell(38, 0).ctype,
                            sheet.cell(39, 0).ctype]
                    if list1.count(1) == 1 and list1.index(1) == 3:
                        myDict['问题8'] = 1
                        count=count+1
                    else:
                        myDict['问题8'] = 0
                    list1.clear()

                    # 第九题
                    list1 = [sheet.cell(41, 0).ctype, sheet.cell(42, 0).ctype, sheet.cell(43, 0).ctype,
                            sheet.cell(44, 0).ctype]
                    if list1.count(1) > 1:
                        myDict['问题9'] = 0
                    elif list1.count(1) == 0:
                        myDict['问题9'] = 0
                    else:
                        index = list1.index(1)
                        myDict['问题9'] = index+1
                    list1.clear()

                    # 第十题（多选）

                    if sheet.cell(52, 0).ctype == 1:
                        myDict['问题10'] = 0
                    else:
                        myDict['问题10'] = 1

                    # 第十一题（多选）

                    if sheet.cell(55, 0).ctype == 1 or  sheet.cell(56, 0).ctype == 1:
                        myDict['问题11'] = 1
                        count=count+1
                    else:
                        myDict['问题11'] = 0

                    # 第十二题（多选）

                    if sheet.cell(60, 0).ctype == 1:
                        myDict['问题12'] = 1
                        count=count+1
                    else:
                        myDict['问题12'] = 0

                    # 第十三题
                    list1 = [sheet.cell(65, 0).ctype, sheet.cell(66, 0).ctype, sheet.cell(67, 0).ctype,
                            sheet.cell(68, 0).ctype]
                    if list1.count(1) > 1:
                        myDict['问题13'] = 0
                    elif list1.count(1) == 0:
                        myDict['问题13'] = 0
                    else:
                        index = list1.index(1)
                        myDict['问题13'] = index+1
                    list1.clear()

                    # 第十四题（多选）
                    if sheet.cell(72, 0).ctype == 1:
                        myDict['问题14'] = 1
                        count=count+1
                    else:
                        myDict['问题14'] = 0

                    # 第十五题
                    list1 = [sheet.cell(76, 0).ctype, sheet.cell(77, 0).ctype, sheet.cell(78, 0).ctype,
                            sheet.cell(79, 0).ctype, sheet.cell(80, 0).ctype]
                    if list1.count(1) > 1:
                        myDict['问题15'] = 0
                    elif list1.count(1) == 0:
                        myDict['问题15'] = 0
                    else:
                        index = list1.index(1)
                        myDict['问题15'] = index+1
                    list1.clear()

                    # 第十六题
                    list1 = [sheet.cell(82, 0).ctype, sheet.cell(83, 0).ctype, sheet.cell(84, 0).ctype,sheet.cell(85, 0).ctype]
                    if list1.count(1) == 1 and list1.index(1) == 2:
                        myDict['问题16'] = 1
                        count=count+1
                    else:
                        myDict['问题16'] = 0
                    list1.clear()

                    # 第十七题（多选）
                    if sheet.cell(90, 0).ctype == 1:
                        myDict['问题17'] = 1
                        count=count+1
                    else:
                        myDict['问题17'] = 0

                    # 第十八题
                    list1 = [sheet.cell(93, 0).ctype, sheet.cell(94, 0).ctype]
                    if list1.count(1) > 1:
                        myDict['问题18'] = 0
                    elif list1.count(1) == 0:
                        myDict['问题18'] = 0
                    else:
                        index = list1.index(1)
                        myDict['问题18'] = index+1
                    list1.clear()

                    # 第十九题
                    list1 = [sheet.cell(96, 0).ctype, sheet.cell(97, 0).ctype, sheet.cell(98, 0).ctype,sheet.cell(99, 0).ctype]
                    if list1.count(1) == 1 and list1.index(1) == 0:
                        myDict['问题19'] = 1
                        count=count+1
                    else:
                        myDict['问题19'] = 0
                    list1.clear()

                    # 第二十题
                    # if sheet.nrows == 103:
                        # print(f"对银行线上渠道和线下渠道的业务受理、办理及信息发布建的建议：{sheet.cell_value(101,1)}")
                    if count >= 5:
                        myDict['问题20'] = 1
                    else:
                        myDict['问题20'] = 0
                        # print(f"没有第二十题")


                    df = pd.DataFrame(data=myDict, index=[0])
                    data = df.to_dict('records')

                    # upload to MongoDB
                    db = client['test4']
                    # print(db)
                    db.data.insert_many(data)
    i=i+1
print('total_number:')
print(total_number)
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
data = pd.read_csv("C://Users//dell//Desktop//银行数据分析//data.csv")
test = pd.read_csv("C://Users//dell//Desktop//银行数据分析//test.csv")
data.describe()
test.describe()

#决策树代码
# coding: utf-8
import csv
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from matplotlib import pyplot as plt
# from sklearn.feature_extraction import DictVectorizer
# from sklearn import preprocessing

from sklearn import tree
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# import pandas as pd
# from graphviz import render, dot
#
# import numpy as np
# from sklearn.utils import graph
#
# import example

y = data['问题20']

X = data.drop(['问题20'], axis=1)
X = X.fillna(0.0).astype(int)

# print(X)

X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=20,  stratify=y, )

# print(y_train.value_counts(normalize=True))
#
# print(y_valid.value_counts(normalize=True))
#
# print(X_valid.shape, y_valid.shape)
# print(X_train.shape, y_train.shape)
#
#
dt_model = DecisionTreeClassifier(max_depth=6,max_leaf_nodes=14, random_state=10)
print(dt_model.fit(X_train, y_train))
print(dt_model.score(X_train, y_train))

print(dt_model.predict(X_valid))
print(dt_model.predict_proba(X_valid))

train_accuracy = []
validation_accuracy = []

for depth in range(2, 20):
    dt_model = DecisionTreeClassifier(max_depth=6, max_leaf_nodes=depth, random_state=10)
    dt_model.fit(X_train, y_train)
    train_accuracy.append(dt_model.score(X_train, y_train))
    validation_accuracy.append(dt_model.score(X_valid, y_valid))

frame = pd.DataFrame({'max_leaf_nodes':range(2, 20), 'train_acc':train_accuracy, 'valid_acc':validation_accuracy})
print(frame.head(20))

plt.figure(figsize=(12, 6))
plt.plot(frame['max_leaf_nodes'], frame['train_acc'], marker='o')
plt.plot(frame['max_leaf_nodes'], frame['valid_acc'], marker='o')
plt.xlabel('Leaf of tree')
plt.ylabel('Performance')
plt.legend(loc='upper right')
plt.show()

decision_tree = tree.export_graphviz(dt_model, out_file='tree.dot', feature_names=X_train.columns,class_names=["No", "Yes"], max_depth=6,filled=False)

plot_confusion_matrix(dt_model, X_train, y_train, display_labels=["NO", "YES"])
plt.show()
print(dt_model.predict(test))




# x=db.data.count_documents({'性别':1,'学历':0,'年龄':0, '问题20':1})
# x1=db.data.count_documents({'性别':1,'学历':0,'年龄':0})
# x2=db.data.count_documents({'性别':1,'学历':0,'年龄':1, '问题20':1})
# x3=db.data.count_documents({'性别':1,'学历':0,'年龄':1})
# x4=db.data.count_documents({'性别':1,'学历':0,'年龄':2, '问题20':1})
# x5=db.data.count_documents({'性别':1,'学历':0,'年龄':2})
# x6=db.data.count_documents({'性别':1,'学历':0,'年龄':3, '问题20':1})
# x7=db.data.count_documents({'性别':1,'学历':0,'年龄':3})
# x8=db.data.count_documents({'性别':1,'学历':0,'年龄':4, '问题20':1})
# x9=db.data.count_documents({'性别':1,'学历':0,'年龄':4})
# x10=db.data.count_documents({'性别':1,'学历':0,'年龄':5, '问题20':1})
# x11=db.data.count_documents({'性别':1,'学历':0,'年龄':5})
a=db.data.count_documents({'性别':1,'学历':1,'年龄':0, '问题20':1})
print('a')
print(a)
a1=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
print(a1)
print(a/a1)
# a2=db.data.count_documents({'性别':1,'学历':1,'年龄':1, '问题20':1})
# a3=db.data.count_documents({'性别':1,'学历':1,'年龄':1})
# a4=db.data.count_documents({'性别':1,'学历':1,'年龄':2, '问题20':1})
# a5=db.data.count_documents({'性别':1,'学历':1,'年龄':2})
# a6=db.data.count_documents({'性别':1,'学历':1,'年龄':3, '问题20':1})
# a7=db.data.count_documents({'性别':1,'学历':1,'年龄':3})
# a8=db.data.count_documents({'性别':1,'学历':1,'年龄':4, '问题20':1})
# a9=db.data.count_documents({'性别':1,'学历':1,'年龄':4})
# a10=db.data.count_documents({'性别':1,'学历':1,'年龄':5, '问题20':1})
# a11=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# b=db.data.count_documents({'性别':1,'学历':2,'年龄':0, '问题20':1})
# b1=db.data.count_documents({'性别':1,'学历':2,'年龄':0})
# b2=db.data.count_documents({'性别':1,'学历':2,'年龄':1, '问题20':1})
# b3=db.data.count_documents({'性别':1,'学历':2,'年龄':1})
# b4=db.data.count_documents({'性别':1,'学历':2,'年龄':2, '问题20':1})
# b5=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# b6=db.data.count_documents({'性别':1,'学历':2,'年龄':3, '问题20':1})
# b7=db.data.count_documents({'性别':1,'学历':2,'年龄':3})
# b8=db.data.count_documents({'性别':1,'学历':2,'年龄':4, '问题20':1})
# b9=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# b10=db.data.count_documents({'性别':1,'学历':2,'年龄':5, '问题20':1})
# b11=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# y=db.data.count_documents({'性别':2,'问题20':1})
# x=db.data.count_documents({'性别':2,'学历':0,'年龄':0, '问题20':1})
# x1=db.data.count_documents({'性别':2,'学历':0,'年龄':0})
# x2=db.data.count_documents({'性别':2,'学历':0,'年龄':1, '问题20':1})
# x3=db.data.count_documents({'性别':2,'学历':0,'年龄':1})
# x4=db.data.count_documents({'性别':2,'学历':0,'年龄':2, '问题20':1})
# x5=db.data.count_documents({'性别':2,'学历':0,'年龄':2})
# x6=db.data.count_documents({'性别':2,'学历':0,'年龄':3, '问题20':1})
# x7=db.data.count_documents({'性别':2,'学历':0,'年龄':3})
# x8=db.data.count_documents({'性别':2,'学历':0,'年龄':4, '问题20':1})
# x9=db.data.count_documents({'性别':2,'学历':0,'年龄':4})
# x10=db.data.count_documents({'性别':2,'学历':0,'年龄':5, '问题20':1})
# x11=db.data.count_documents({'性别':2,'学历':0,'年龄':5})
# a=db.data.count_documents({'性别':2,'学历':0,'年龄':0, '问题20':1})
# a1=db.data.count_documents({'性别':2,'学历':1,'年龄':0})

# a2=db.data.count_documents({'性别':2,'学历':1,'年龄':1, '问题20':1})
# a3=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# a4=db.data.count_documents({'性别':2,'学历':1,'年龄':2, '问题20':1})
# a5=db.data.count_documents({'性别':2,'学历':1,'年龄':2})
# a6=db.data.count_documents({'性别':2,'学历':1,'年龄':3, '问题20':1})
# a7=db.data.count_documents({'性别':2,'学历':1,'年龄':3})
# a8=db.data.count_documents({'性别':2,'学历':1,'年龄':4, '问题20':1})
# a9=db.data.count_documents({'性别':2,'学历':1,'年龄':4})
# a10=db.data.count_documents({'性别':2,'学历':1,'年龄':5, '问题20':1})
# a11=db.data.count_documents({'性别':2,'学历':1,'年龄':5})
# b=db.data.count_documents({'性别':2,'学历':2,'年龄':0, '问题20':1})
# b1=db.data.count_documents({'性别':2,'学历':2,'年龄':0})
# b2=db.data.count_documents({'性别':2,'学历':2,'年龄':1, '问题20':1})
# b3=db.data.count_documents({'性别':2,'学历':2,'年龄':1})
# b4=db.data.count_documents({'性别':2,'学历':2,'年龄':2, '问题20':1})
# b5=db.data.count_documents({'性别':2,'学历':2,'年龄':2})
# b6=db.data.count_documents({'性别':2,'学历':2,'年龄':3, '问题20':1})
# b7=db.data.count_documents({'性别':2,'学历':2,'年龄':3})
# b8=db.data.count_documents({'性别':2,'学历':2,'年龄':4, '问题20':1})
# b9=db.data.count_documents({'性别':2,'学历':2,'年龄':4})
# b10=db.data.count_documents({'性别':2,'学历':2,'年龄':5, '问题20':1})
# b11=db.data.count_documents({'性别':2,'学历':2,'年龄':5})
# print(1)
# print(x/x1)
# print(x2/x3)
# print(x4/x5)
# print(x6/x7)
# print(x8/x9)
# print(x10/x11)
# print(2)
# print(a/a1)
# print(a2/a3)
# print(a4/a5)
# print(a6/a7)
# print(a8/a9)
# print(a10/a11)
# print(3)
# print(b/b1)
# print(b2/b3)
# print(b4/b5)
# print(b6/b7)
# print(b8/b9)
# print(b10/b11)
# print(b)
# print(b1)



# aa1=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
# aa2=db.data.count_documents({'性别':1,'学历':1,'年龄':0,'问题6':1})
# aa3=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
# aa4=db.data.count_documents({'性别':1,'学历':1,'年龄':0,'问题7':1})
# aa5=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
# aa6=db.data.count_documents({'性别':1,'学历':1,'年龄':0,'问题8':1})
# aa7=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
# aa8=db.data.count_documents({'性别':1,'学历':1,'年龄':0,'问题11':1})
# aa9=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
# aa10=db.data.count_documents({'性别':1,'学历':1,'年龄':0,'问题12':1})
# aa11=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
# aa12=db.data.count_documents({'性别':1,'学历':1,'年龄':0,'问题14':1})
# aa13=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
# aa14=db.data.count_documents({'性别':1,'学历':1,'年龄':0,'问题16':1})
# aa15=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
# aa16=db.data.count_documents({'性别':1,'学历':1,'年龄':0,'问题17':1})
# aa17=db.data.count_documents({'性别':1,'学历':1,'年龄':0})
# aa18=db.data.count_documents({'性别':1,'学历':1,'年龄':0,'问题19':1})
# print(aa2/aa1)
# print(aa4/aa3)
# print(aa6/aa5)
# print(aa8/aa7)
# print(aa10/aa9)
# print(aa12/aa11)
# print(aa14/aa13)
# print(aa16/aa15)
# print(aa18/aa17)


# aa1=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# aa2=db.data.count_documents({'性别':1,'学历':1,'年龄':5,'问题6':1})
# aa3=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# aa4=db.data.count_documents({'性别':1,'学历':1,'年龄':5,'问题7':1})
# aa5=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# aa6=db.data.count_documents({'性别':1,'学历':1,'年龄':5,'问题8':1})
# aa7=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# aa8=db.data.count_documents({'性别':1,'学历':1,'年龄':5,'问题11':1})
# aa9=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# aa10=db.data.count_documents({'性别':1,'学历':1,'年龄':5,'问题12':1})
# aa11=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# aa12=db.data.count_documents({'性别':1,'学历':1,'年龄':5,'问题14':1})
# aa13=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# aa14=db.data.count_documents({'性别':1,'学历':1,'年龄':5,'问题16':1})
# aa15=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# aa16=db.data.count_documents({'性别':1,'学历':1,'年龄':5,'问题17':1})
# aa17=db.data.count_documents({'性别':1,'学历':1,'年龄':5})
# aa18=db.data.count_documents({'性别':1,'学历':1,'年龄':5,'问题19':1})
# print(aa2/aa1)
# print(aa4/aa3)
# print(aa6/aa5)
# print(aa8/aa7)
# print(aa10/aa9)
# print(aa12/aa11)
# print(aa14/aa13)
# print(aa16/aa15)
# print(aa18/aa17)

# aa1=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# aa2=db.data.count_documents({'性别':1,'学历':2,'年龄':2,'问题6':1})
# aa3=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# aa4=db.data.count_documents({'性别':1,'学历':2,'年龄':2,'问题7':1})
# aa5=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# aa6=db.data.count_documents({'性别':1,'学历':2,'年龄':2,'问题8':1})
# aa7=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# aa8=db.data.count_documents({'性别':1,'学历':2,'年龄':2,'问题11':1})
# aa9=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# aa10=db.data.count_documents({'性别':1,'学历':2,'年龄':2,'问题12':1})
# aa11=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# aa12=db.data.count_documents({'性别':1,'学历':2,'年龄':2,'问题14':1})
# aa13=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# aa14=db.data.count_documents({'性别':1,'学历':2,'年龄':2,'问题16':1})
# aa15=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# aa16=db.data.count_documents({'性别':1,'学历':2,'年龄':2,'问题17':1})
# aa17=db.data.count_documents({'性别':1,'学历':2,'年龄':2})
# aa18=db.data.count_documents({'性别':1,'学历':2,'年龄':2,'问题19':1})
# print(aa2/aa1)
# print(aa4/aa3)
# print(aa6/aa5)
# print(aa8/aa7)
# print(aa10/aa9)
# print(aa12/aa11)
# print(aa14/aa13)
# print(aa16/aa15)
# print(aa18/aa17)

# aa1=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# aa2=db.data.count_documents({'性别':1,'学历':2,'年龄':4,'问题6':1})
# aa3=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# aa4=db.data.count_documents({'性别':1,'学历':2,'年龄':4,'问题7':1})
# aa5=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# aa6=db.data.count_documents({'性别':1,'学历':2,'年龄':4,'问题8':1})
# aa7=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# aa8=db.data.count_documents({'性别':1,'学历':2,'年龄':4,'问题11':1})
# aa9=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# aa10=db.data.count_documents({'性别':1,'学历':2,'年龄':4,'问题12':1})
# aa11=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# aa12=db.data.count_documents({'性别':1,'学历':2,'年龄':4,'问题14':1})
# aa13=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# aa14=db.data.count_documents({'性别':1,'学历':2,'年龄':4,'问题16':1})
# aa15=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# aa16=db.data.count_documents({'性别':1,'学历':2,'年龄':4,'问题17':1})
# aa17=db.data.count_documents({'性别':1,'学历':2,'年龄':4})
# aa18=db.data.count_documents({'性别':1,'学历':2,'年龄':4,'问题19':1})
# print(aa2/aa1)
# print(aa4/aa3)
# print(aa6/aa5)
# print(aa8/aa7)
# print(aa10/aa9)
# print(aa12/aa11)
# print(aa14/aa13)
# print(aa16/aa15)
# print(aa18/aa17)

# aa1=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# aa2=db.data.count_documents({'性别':1,'学历':2,'年龄':5,'问题6':1})
# aa3=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# aa4=db.data.count_documents({'性别':1,'学历':2,'年龄':5,'问题7':1})
# aa5=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# aa6=db.data.count_documents({'性别':1,'学历':2,'年龄':5,'问题8':1})
# aa7=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# aa8=db.data.count_documents({'性别':1,'学历':2,'年龄':5,'问题11':1})
# aa9=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# aa10=db.data.count_documents({'性别':1,'学历':2,'年龄':5,'问题12':1})
# aa11=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# aa12=db.data.count_documents({'性别':1,'学历':2,'年龄':5,'问题14':1})
# aa13=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# aa14=db.data.count_documents({'性别':1,'学历':2,'年龄':5,'问题16':1})
# aa15=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# aa16=db.data.count_documents({'性别':1,'学历':2,'年龄':5,'问题17':1})
# aa17=db.data.count_documents({'性别':1,'学历':2,'年龄':5})
# aa18=db.data.count_documents({'性别':1,'学历':2,'年龄':5,'问题19':1})
# print(aa2/aa1)
# print(aa4/aa3)
# print(aa6/aa5)
# print(aa8/aa7)
# print(aa10/aa9)
# print(aa12/aa11)
# print(aa14/aa13)
# print(aa16/aa15)
# print(aa18/aa17)

# aa1=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# aa2=db.data.count_documents({'性别':2,'学历':1,'年龄':1,'问题6':1})
# aa3=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# aa4=db.data.count_documents({'性别':2,'学历':1,'年龄':1,'问题7':1})
# aa5=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# aa6=db.data.count_documents({'性别':2,'学历':1,'年龄':1,'问题8':1})
# aa7=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# aa8=db.data.count_documents({'性别':2,'学历':1,'年龄':1,'问题11':1})
# aa9=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# aa10=db.data.count_documents({'性别':2,'学历':1,'年龄':1,'问题12':1})
# aa11=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# aa12=db.data.count_documents({'性别':2,'学历':1,'年龄':1,'问题14':1})
# aa13=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# aa14=db.data.count_documents({'性别':2,'学历':1,'年龄':1,'问题16':1})
# aa15=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# aa16=db.data.count_documents({'性别':2,'学历':1,'年龄':1,'问题17':1})
# aa17=db.data.count_documents({'性别':2,'学历':1,'年龄':1})
# aa18=db.data.count_documents({'性别':2,'学历':1,'年龄':1,'问题19':1})
# print(aa2/aa1)
# print(aa4/aa3)
# print(aa6/aa5)
# print(aa8/aa7)
# print(aa10/aa9)
# print(aa12/aa11)
# print(aa14/aa13)
# print(aa16/aa15)
# print(aa18/aa17)