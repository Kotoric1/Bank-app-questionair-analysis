
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
#
                    if sheet.cell(46, 0).ctype == 1:
                        myDict['问题10A'] = 1

                    if sheet.cell(47, 0).ctype == 1:
                        myDict['问题10B'] = 1

                    if sheet.cell(48, 0).ctype == 1:
                        myDict['问题10C'] = 1

                    if sheet.cell(49, 0).ctype == 1:
                        myDict['问题10D'] = 1

                    if sheet.cell(50, 0).ctype == 1:
                        myDict['问题10E'] = 1

                    if sheet.cell(51, 0).ctype == 1:
                        myDict['问题10F'] = 1

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

                    client = MongoClient('localhost', 27017)
                    new_file = file.split('(', 1)[0]

                    if new_file == '区域1 ':
                        # upload to MongoDB
                        db = client['地域1']
                        # print(db)
                        db.data.insert_many(data)
                    elif new_file == '区域2 ':
                        # upload to MongoDB
                        db = client['地域2']
                        # print(db)
                        db.data.insert_many(data)
                    elif new_file == '区域3 ':
                        # upload to MongoDB
                        db = client['地域3']
                        # print(db)
                        db.data.insert_many(data)
                    elif new_file == '区域4 ':
                        # upload to MongoDB
                        db = client['地域4']
                        # print(db)
                        db.data.insert_many(data)
    i=i+1
#print(f"count:{count}")
#print(f"男:{male}")
#print(f"女:{female}")
#print(f"未填写性别：{none}")
#print(f"性别多选:{false}")

#使能输入中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data1 = pd.read_csv("C://Users//dell//Desktop//银行数据分析//地域1.csv")
data2 = pd.read_csv("C://Users//dell//Desktop//银行数据分析//地域2.csv")
data3 = pd.read_csv("C://Users//dell//Desktop//银行数据分析//地域3.csv")
data4 = pd.read_csv("C://Users//dell//Desktop//银行数据分析//地域4.csv")

# a = len(data1.loc[data1['问题20'] == 1])
# print(a/len(data1))
# b = len(data2.loc[data2['问题20'] == 1])
# print(b/len(data2))
# c = len(data3.loc[data3['问题20'] == 1])
# print(c/len(data3))
# d = len(data4.loc[data4['问题20'] == 1])
# print(d/len(data4))
#
# A = ('区域1', '区域2', '区域3', '区域4')
# number = [a/len(data1), b/len(data2), c/len(data3), d/len(data4)]
# plt.bar(A, number)
# plt.title('每个地域手机银行APP的潜在客服百分比')
# plt.show()

e = data3.loc[data3['问题20'] == 1]
f1 = e.loc[e['性别'] == 1]
f2 = e.loc[e['性别'] == 2]
g1 = data3.loc[data3['学历'] == 0]
g2 = data3.loc[data3['学历'] == 1]
g3 = data3.loc[data3['学历'] == 2]
h1 = data3.loc[data3['年龄'] == 0]
h2 = data3.loc[data3['年龄'] == 1]
h3 = data3.loc[data3['年龄'] == 2]
h4 = data3.loc[data3['年龄'] == 3]
h5 = data3.loc[data3['年龄'] == 4]
h6 = data3.loc[data3['年龄'] == 5]
b1 = data3.loc[data3['问题10A'] == 1]
b2 = data3.loc[data3['问题10B'] == 1]
b3 = data3.loc[data3['问题10C'] == 1]
b4 = data3.loc[data3['问题10D'] == 1]
b5 = data3.loc[data3['问题10E'] == 1]
b6 = data3.loc[data3['问题10F'] == 1]
print(len(f1))
print(len(f2))

i = data2.loc[data2['问题20'] == 1]
j1 = i.loc[i['性别'] == 1]
j2 = i.loc[i['性别'] == 2]
k1 = data2.loc[data2['学历'] == 0]
k2 = data2.loc[data2['学历'] == 1]
k3 = data2.loc[data2['学历'] == 2]
l1 = data2.loc[data2['年龄'] == 0]
l2 = data2.loc[data2['年龄'] == 1]
l3 = data2.loc[data2['年龄'] == 2]
l4 = data2.loc[data2['年龄'] == 3]
l5 = data2.loc[data2['年龄'] == 4]
l6 = data2.loc[data2['年龄'] == 5]
a1 = data2.loc[data2['问题10A'] == 1]
a2 = data2.loc[data2['问题10B'] == 1]
a3 = data2.loc[data2['问题10C'] == 1]
a4 = data2.loc[data2['问题10D'] == 1]
a5 = data2.loc[data2['问题10E'] == 1]
a6 = data2.loc[data2['问题10F'] == 1]
print(len(j1))
print(len(j2))

m = data1.loc[data1['问题20'] == 1]
n1 = m.loc[m['性别'] == 1]
n2 = m.loc[m['性别'] == 2]
o1 = data1.loc[data1['学历'] == 0]
o2 = data1.loc[data1['学历'] == 1]
o3 = data1.loc[data1['学历'] == 2]
p1 = data1.loc[data1['年龄'] == 0]
p2 = data1.loc[data1['年龄'] == 1]
p3 = data1.loc[data1['年龄'] == 2]
p4 = data1.loc[data1['年龄'] == 3]
p5 = data1.loc[data1['年龄'] == 4]
p6 = data1.loc[data1['年龄'] == 5]
c1 = data1.loc[data1['问题10A'] == 1]
c2 = data1.loc[data1['问题10B'] == 1]
c3 = data1.loc[data1['问题10C'] == 1]
c4 = data1.loc[data1['问题10D'] == 1]
c5 = data1.loc[data1['问题10E'] == 1]
c6 = data1.loc[data1['问题10F'] == 1]
print(len(n1))
print(len(n2))

q = data4.loc[data4['问题20'] == 1]
r1 = q.loc[q['性别'] == 1]
r2 = q.loc[q['性别'] == 2]
s1 = data4.loc[data4['学历'] == 0]
s2 = data4.loc[data4['学历'] == 1]
s3 = data4.loc[data4['学历'] == 2]
t1 = data4.loc[data4['年龄'] == 0]
t2 = data4.loc[data4['年龄'] == 1]
t3 = data4.loc[data4['年龄'] == 2]
t4 = data4.loc[data4['年龄'] == 3]
t5 = data4.loc[data4['年龄'] == 4]
t6 = data4.loc[data4['年龄'] == 5]
d1 = data4.loc[data4['问题10A'] == 1]
d2 = data4.loc[data4['问题10B'] == 1]
d3 = data4.loc[data4['问题10C'] == 1]
d4 = data4.loc[data4['问题10D'] == 1]
d5 = data4.loc[data4['问题10E'] == 1]
d6 = data4.loc[data4['问题10F'] == 1]
print(len(r1))
print(len(r2))



# Times=('区域1','区域2','区域3','区域4')
# AAA=[len(n1),len(j1),len(f1),len(r1)]
# BBB=[len(n2),len(j2),len(f2),len(r2)]
# bar_width=0.4
# index_AAA = np.arange(len(Times))
# index_BBB = index_AAA + bar_width
# plt.bar(index_AAA, height=AAA, width=bar_width, color='b', label='男')
# plt.bar(index_BBB, height=BBB, width=bar_width, color='g', label='女')
# plt.legend()
# plt.xticks(index_AAA + bar_width/2, Times)
# plt.ylabel('人数') # 纵坐标轴标题
# plt.title('不同区域下男女潜在客户人数')
# plt.xticks(rotation=-15)
# plt.show()


# Times=('区域1','区域2','区域3','区域4')
# AAA=[len(o1),len(k1),len(g1),len(s1)]
# BBB=[len(o2),len(k2),len(g2),len(s2)]
# CCC=[len(o3),len(k3),len(g3),len(s3)]
# bar_width=0.2
# index_AAA = np.arange(len(Times))
# index_BBB = index_AAA + bar_width
# index_CCC = index_BBB + bar_width
# plt.bar(index_AAA, height=AAA, width=bar_width, color='b', label='高中及以下')
# plt.bar(index_BBB, height=BBB, width=bar_width, color='g', label='本科及专科')
# plt.bar(index_CCC, height=CCC, width=bar_width, color='g', label='研究生及以上')
# plt.legend()
# plt.xticks(index_AAA + bar_width/2, Times)
# plt.ylabel('人数') # 纵坐标轴标题
# plt.title('不同区域下不同学历潜在客户人数')
# plt.xticks(rotation=-15)
# plt.show()

# Times=('区域1','区域2','区域3','区域4')
# AAA=[len(p1),len(l1),len(h1),len(t1)]
# BBB=[len(p2),len(l2),len(h2),len(t2)]
# CCC=[len(p3),len(l3),len(h3),len(t3)]
# DDD=[len(p4),len(l4),len(h4),len(t4)]
# EEE=[len(p5),len(l5),len(h5),len(t5)]
# FFF=[len(p6),len(l6),len(h6),len(t6)]
# bar_width=0.1
# index_AAA = np.arange(len(Times))
# index_BBB = index_AAA + bar_width
# index_CCC = index_BBB + bar_width
# index_DDD = index_CCC + bar_width
# index_EEE = index_DDD + bar_width
# index_FFF = index_EEE + bar_width
# plt.bar(index_AAA, height=AAA, width=bar_width, color='b', label='20岁及以下')
# plt.bar(index_BBB, height=BBB, width=bar_width, color='g', label='20-30岁')
# plt.bar(index_CCC, height=CCC, width=bar_width, color='r', label='30-40岁')
# plt.bar(index_DDD, height=DDD, width=bar_width, color='c', label='40-50岁')
# plt.bar(index_EEE, height=EEE, width=bar_width, color='m', label='50-60岁')
# plt.bar(index_FFF, height=FFF, width=bar_width, color='y', label='60岁及以上')
# plt.legend()
# plt.xticks(index_FFF + bar_width/2, Times)
# plt.ylabel('人数') # 纵坐标轴标题
# plt.title('不同区域下不同年龄潜在客户人数')
# plt.xticks(rotation=-15)
# plt.show()

Times=('区域1','区域2','区域3','区域4')
AAA=[len(c1),len(a1),len(b1),len(d1)]
BBB=[len(c2),len(a2),len(b2),len(d2)]
CCC=[len(c3),len(a3),len(b3),len(d3)]
DDD=[len(c4),len(a4),len(b4),len(d4)]
EEE=[len(c5),len(a5),len(b5),len(d5)]
FFF=[len(c6),len(a6),len(b6),len(d6)]
bar_width=0.1
index_AAA = np.arange(len(Times))
index_BBB = index_AAA + bar_width
index_CCC = index_BBB + bar_width
index_DDD = index_CCC + bar_width
index_EEE = index_DDD + bar_width
index_FFF = index_EEE + bar_width
plt.bar(index_AAA, height=AAA, width=bar_width, color='b', label='转账支付')
plt.bar(index_BBB, height=BBB, width=bar_width, color='g', label='贷款')
plt.bar(index_CCC, height=CCC, width=bar_width, color='r', label='基金或投资理财')
plt.bar(index_DDD, height=DDD, width=bar_width, color='c', label='查询账户')
plt.bar(index_EEE, height=EEE, width=bar_width, color='m', label='生活缴费')
plt.bar(index_FFF, height=FFF, width=bar_width, color='y', label='优惠卷')
plt.legend()
plt.xticks(index_CCC + bar_width/2, Times)
plt.ylabel('人数') # 纵坐标轴标题
plt.title('不同区域使用手机银行APP的原因')
plt.xticks(rotation=-15)
plt.show()