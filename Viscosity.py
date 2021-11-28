import os

import pandas as pd
import xlrd
from matplotlib import pyplot as plt
from pymongo import MongoClient

aa=0
ab=0
ac=0
ad=0
ae=0
af=0
male=0
female=0
none=0
false=0
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
                    if sheet.cell(46, 0).ctype == 1:
                        myDict['问题10A'] = 1
                        aa=aa+1
                    if sheet.cell(47, 0).ctype == 1:
                        myDict['问题10B'] = 1
                        ab = ab + 1
                    if sheet.cell(48, 0).ctype == 1:
                        myDict['问题10C'] = 1
                        ac = ac + 1
                    if sheet.cell(49, 0).ctype == 1:
                        myDict['问题10D'] = 1
                        ad = ad + 1
                    if sheet.cell(50, 0).ctype == 1:
                        myDict['问题10E'] = 1
                        ae = ae + 1
                    if sheet.cell(51, 0).ctype == 1:
                        myDict['问题10F'] = 1
                        af = af + 1

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
                    db = client['test5']
                    # print(db)
                    db.data.insert_many(data)
    i=i+1



# x=db.data.count_documents({'性别':1, '问题10A':1})
# # y=db.data.count_documents({'性别':2, '问题10A':1})
# # a=db.data.count_documents({'年龄':0, '问题10A':1})
# # b=db.data.count_documents({'年龄':1, '问题10A':1})
# # c=db.data.count_documents({'年龄':2, '问题10A':1})
# # d=db.data.count_documents({'年龄':3, '问题10A':1})
# # e=db.data.count_documents({'年龄':4, '问题10A':1})
# # f=db.data.count_documents({'年龄':5, '问题10A':1})
# # g=db.data.count_documents({'学历':0, '问题10A':1})
# # h=db.data.count_documents({'学历':1, '问题10A':1})
# # i=db.data.count_documents({'学历':2, '问题10A':1})

# x=db.data.count_documents({'性别':1, '问题10C':1})
# y=db.data.count_documents({'性别':2, '问题10C':1})
# a=db.data.count_documents({'年龄':0, '问题10C':1})
# b=db.data.count_documents({'年龄':1, '问题10C':1})
# c=db.data.count_documents({'年龄':2, '问题10C':1})
# d=db.data.count_documents({'年龄':3, '问题10C':1})
# e=db.data.count_documents({'年龄':4, '问题10C':1})
# f=db.data.count_documents({'年龄':5, '问题10C':1})
# g=db.data.count_documents({'学历':0, '问题10C':1})
# h=db.data.count_documents({'学历':1, '问题10C':1})
# i=db.data.count_documents({'学历':2, '问题10C':1})

x=db.data.count_documents({'性别':1, '问题10D':1})
y=db.data.count_documents({'性别':2, '问题10D':1})
a=db.data.count_documents({'年龄':0, '问题10D':1})
b=db.data.count_documents({'年龄':1, '问题10D':1})
c=db.data.count_documents({'年龄':2, '问题10D':1})
d=db.data.count_documents({'年龄':3, '问题10D':1})
e=db.data.count_documents({'年龄':4, '问题10D':1})
f=db.data.count_documents({'年龄':5, '问题10D':1})
g=db.data.count_documents({'学历':0, '问题10D':1})
h=db.data.count_documents({'学历':1, '问题10D':1})
i=db.data.count_documents({'学历':2, '问题10D':1})

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#
labels='男','女'
size=[x,y]
explode=(0,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('因为查询账户使用手机银行APP的人群的男女分布')
plt.savefig('因为查询账户使用手机银行APP的人群的男女分布.jpg')
plt.show()

labels='高中及以下','研究生及以上','本科及专科'
size=[g,i,h]
explode=(0,0,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('因为查询账户使用手机银行APP的人群的学历分布')
plt.savefig('因为查询账户使用手机银行APP的人群的学历分布.jpg')
plt.show()
#
A = ('20岁以下', '20-30', '30-40', '40-50', '50-60','60岁以上')
number = [a,b,c,d,e,f]
plt.bar(A, number)
plt.title('因为查询账户使用手机银行APP的人群的年龄分布')
plt.savefig('因为查询账户使用手机银行APP的人群的年龄分布.jpg')
plt.show()

B = ('转账支付', '贷款相关', '基金或投资理财', '查询账户', '生活缴费','优惠卷')
number = [aa,ab,ac,ad,ae,af]
plt.bar(B, number)
plt.xticks(rotation=-15)
plt.title('使用手机银行APP的原因')
plt.savefig('使用手机银行APP的原因.jpg')
plt.show()

