
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import numpy as np
import matplotlib.pyplot as plt
import os
import xlrd
import pandas as pd
from pymongo import MongoClient
import statsmodels.api as sm


count=0
male=0
female=0
none=0
false=0
aa=0
ab=0
ac=0
ad=0
ae=0
af=0
ag=0
ba=0
bb=0
bc=0
bd=0
ca=0
cb=0
cc=0
cd=0
ce=0
da=0
dg=0
dc=0
dd=0
de=0
ea=0
eb=0
ec=0
ed=0
ee=0

path="C://Users//dell//Desktop//银行数据分析-----中科院软件所//原始数据与要求//原始数据集"
upath=path.encode('utf-8').decode('utf-8')
dirs=os.listdir(upath)


for file in dirs:
    count = count + 1
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
                    myDict={}
                    #print(f"表单名：{sheet.name}")
                    myDict['姓名']=sheet.name
                    #第一题
                    if sheet.cell(3,0).ctype==1:
                        if sheet.cell(4, 0).ctype == 1:
                            #print(f"性别：单选题多选")
                            myDict['性别']='单选题多选'
                            false=false+1
                        else:
                            male=male+1
                            #print('性别：男')
                            myDict['性别']='男'
                    else:
                        if sheet.cell(4,0).ctype==0:
                            #print(f"性别：未填写")
                            none=none+1
                            myDict['性别']='未填写'
                        else:
                            #print(f"性别：女")
                            female = female + 1
                            myDict['性别']='女'
                    #第二题
                    list=[sheet.cell(6,0).ctype,sheet.cell(7,0).ctype,sheet.cell(8,0).ctype,sheet.cell(9,0).ctype,sheet.cell(10,0).ctype,sheet.cell(11,0).ctype]
                    if list.count(1)>1:
                        myDict['年龄'] ='单选题多选'
                    elif list.count(1)==0:
                        myDict['年龄'] = '未填写'
                    else:
                        index = list.index(1) + 6
                        myDict['年龄'] = sheet.cell_value(index,2)
                    list.clear()

                    #第三题
                    list=[sheet.cell(13,0).ctype,sheet.cell(14,0).ctype,sheet.cell(15, 0).ctype]
                    if list.count(1) > 1:
                        myDict['学历'] = '单选题多选'
                    elif list.count(1) == 0:
                        myDict['学历'] = '未填写'
                    else:
                        index = list.index(1) + 13
                        myDict['学历'] = sheet.cell_value(index, 2)
                    list.clear()

                    # 第四题
                    list = [sheet.cell(17, 0).ctype, sheet.cell(18, 0).ctype, sheet.cell(19, 0).ctype]
                    if list.count(1) > 1:
                        myDict['每月去网点次数'] = '单选题多选'
                    elif list.count(1) == 0:
                        myDict['每月去网点次数'] = '未填写'
                    else:
                        index = list.index(1) + 17
                        myDict['每月去网点次数'] = sheet.cell_value(index, 2)
                    list.clear()

                    # 第五题
                    list = [sheet.cell(21, 0).ctype, sheet.cell(22, 0).ctype, sheet.cell(23, 0).ctype]
                    if list.count(1) > 1:
                        myDict['最常用的手机银行每月使用次数'] = '单选题多选'
                    elif list.count(1) == 0:
                        myDict['最常用的手机银行每月使用次数'] = '未填写'
                    else:
                        index = list.index(1) + 21
                        myDict['最常用的手机银行每月使用次数'] = sheet.cell_value(index, 2)
                    list.clear()

                    # 第六题
                    list = [sheet.cell(25, 0).ctype, sheet.cell(26, 0).ctype, sheet.cell(27, 0).ctype,
                            sheet.cell(28, 0).ctype]
                    if list.count(1) > 1:
                        myDict['日常生活消费常用支付方式'] = '单选题多选'
                    elif list.count(1) == 0:
                        myDict['日常生活消费常用支付方式'] = '未填写'
                    else:
                        index = list.index(1) + 25
                        myDict['日常生活消费常用支付方式'] = sheet.cell_value(index, 2)
                    list.clear()

                    # 第七题
                    list = [sheet.cell(30, 0).ctype, sheet.cell(31, 0).ctype, sheet.cell(32, 0).ctype,
                            sheet.cell(33, 0).ctype, sheet.cell(34, 0).ctype]
                    if list.count(1) > 1:
                        myDict['常用方式查询银行账户余额'] = '单选题多选'
                    elif list.count(1) == 0:
                        myDict['常用方式查询银行账户余额'] = '未填写'
                    else:
                        index = list.index(1) + 30
                        myDict['常用方式查询银行账户余额'] = sheet.cell_value(index, 2)
                    list.clear()

                    # 第八题
                    list = [sheet.cell(36, 0).ctype, sheet.cell(37, 0).ctype, sheet.cell(38, 0).ctype,
                            sheet.cell(39, 0).ctype]
                    if list.count(1) > 1:
                        myDict['最常用办理银行业务的方式'] = '单选题多选'
                    elif list.count(1) == 0:
                        myDict['最常用办理银行业务的方式'] = '未填写'
                    else:
                        index = list.index(1) + 36
                        myDict['最常用办理银行业务的方式'] = sheet.cell_value(index, 2)
                    list.clear()

                    # 第九题
                    list = [sheet.cell(41, 0).ctype, sheet.cell(42, 0).ctype, sheet.cell(43, 0).ctype,
                            sheet.cell(44, 0).ctype]
                    if list.count(1) > 1:
                        myDict['银行网点使用最多的业务'] = '单选题多选'
                    elif list.count(1) == 0:
                        myDict['银行网点使用最多的业务'] = '未填写'
                    else:
                        index = list.index(1) + 41
                        myDict['银行网点使用最多的业务'] = sheet.cell_value(index, 2)
                    list.clear()

                    # 第十题（多选）
                    if sheet.cell(46, 0).ctype == 1:
                        a = "转账支付, "
                        aa=aa+1
                    else:
                        a = ""
                    if sheet.cell(47, 0).ctype == 1:
                        b = "贷款相关, "
                        ab=ab+1
                    else:
                        b = ""
                    if sheet.cell(48, 0).ctype == 1:
                        c = "基金或投资理财类, "
                        ac=ac+1
                    else:
                        c = ""
                    if sheet.cell(49, 0).ctype == 1:
                        d = "查询账户等其他, "
                        ad=ad+1
                    else:
                        d = ""
                    if sheet.cell(50, 0).ctype == 1:
                        e = "生活缴费, "
                        ae=ae+1
                    else:
                        e = ""
                    if sheet.cell(51, 0).ctype == 1:
                        f = "领用银行发放的优惠卷, "
                        af=af+1
                    else:
                        f = ""
                    if sheet.cell(52, 0).ctype == 1:
                        g = "不使用手机银行, "
                        ag=ag+1
                    else:
                        g = ""
                    if a == "" and b == "" and c == "" and d == "" and e == "" and f == "" and g == "":
                        # print(f"登录某家银行的手机银行APP一般使用的功能：未填写")
                        myDict['登录某家银行的手机银行APP一般使用的功能'] = '未填写'
                    else:
                        # print(f"登录某家银行的手机银行APP一般使用的功能：{a+b+c+d+e+f+g}")
                        Ans=a + b + c + d + e + f + g
                        myDict['登录某家银行的手机银行APP一般使用的功能'] = Ans

                        # 第十一题（多选）
                        if sheet.cell(54, 0).ctype == 1:
                            a = "更看重线下网点渠道的服务水平，网点多、离家近、服务好的银行，偏好到网点面对面办理, "
                            ba=ba+1
                        else:
                            a = ""
                        if sheet.cell(55, 0).ctype == 1:
                            b = "更看重手机银行渠道的便捷性，线上渠道多又全、便捷高效，偏好通过手机银行等渠道自助办理, "
                            bb=bb+1
                        else:
                            b = ""
                        if sheet.cell(56, 0).ctype == 1:
                            c = "更看重各渠道服务相互结合，即可客户经理专属咨询，又可通过手机等线上渠道便捷办理, "
                            bc=bc+1
                        else:
                            c = ""
                        if sheet.cell(57, 0).ctype == 1:
                            d = "不在乎什么渠道，更看重产品是不是有竞争力，是否满足我的需求, "
                            bd=bd+1
                        else:
                            d = ""
                        if a == "" and b == "" and c == "" and d == "":
                            # print(f"选择银行服务时更看重的渠道：未填写")
                            myDict['选择银行服务时更看重的渠道'] = '未填写'
                        else:
                            # print(f"选择银行服务时更看重的渠道：{a+b+c+d}")
                            Ans=a+b+c+d
                            myDict['选择银行服务时更看重的渠道'] = Ans

                        # 第十二题（多选）
                        if sheet.cell(59, 0).ctype == 1:
                            a = "银行网点, "
                            ca=ca+1
                        else:
                            a = ""
                        if sheet.cell(60, 0).ctype == 1:
                            b = "手机银行, "
                            cb=cb+1
                        else:
                            b = ""
                        if sheet.cell(61, 0).ctype == 1:
                            c = "朋友圈, "
                            cc=cc+1
                        else:
                            c = ""
                        if sheet.cell(62, 0).ctype == 1:
                            d = "银行人员的外拓服务, "
                            cd=cd+1
                        else:
                            d = ""
                        if sheet.cell(63, 0).ctype == 1:
                            e = "各类生活场景, "
                            ce=ce+1
                        else:
                            e = ""
                        if a == "" and b == "" and c == "" and d == "" and e == "":
                            # print(f"希望参与并享受银行优惠促销活动的渠道：未填写")
                            myDict['登录某家银行的手机银行APP一般使用的功能'] = '未填写'
                        else:
                            # print(f"希望参与并享受银行优惠促销活动的渠道：{a+b+c+d+e}")
                            Ans=a+b+c+d+e
                            myDict['登录某家银行的手机银行APP一般使用的功能'] = Ans

                        # 第十三题
                        list = [sheet.cell(65, 0).ctype, sheet.cell(66, 0).ctype, sheet.cell(67, 0).ctype,
                                sheet.cell(68, 0).ctype]
                        if list.count(1) > 1:
                            myDict['选择银行的业务办理渠道的原因'] = '单选题多选'
                        elif list.count(1) == 0:
                            myDict['选择银行的业务办理渠道的原因'] = '未填写'
                        else:
                            index = list.index(1) + 65
                            myDict['选择银行的业务办理渠道的原因'] = sheet.cell_value(index, 2)
                        list.clear()

                        # 第十四题（多选）
                        if sheet.cell(70, 0).ctype == 1:
                            a = "基金等投资理财类, "
                            da = da+1
                        else:
                            a = ""
                        if sheet.cell(71, 0).ctype == 1:
                            b = "消费贷款, "
                            dg = dg+1
                        else:
                            b = ""
                        if sheet.cell(72, 0).ctype == 1:
                            c = "手机银行或者网上银行, "
                            dc = dc+1
                        else:
                            c = ""
                        if sheet.cell(73, 0).ctype == 1:
                            d = "信用卡透支, "
                            dd = dd+1
                        else:
                            d = ""
                        if sheet.cell(74, 0).ctype == 1:
                            e = "仅存取款, "
                            de=de+1
                        else:
                            e = ""
                        if a == "" and b == "" and c == "" and d == "" and e == "":
                            # print(f"目前在使用的银行产品：未填写")
                            myDict['目前在使用的银行产品'] = '未填写'
                        else:
                            # print(f"目前在使用的银行产品：{a+b+c+d+e}")
                            Ans=a + b + c + d + e
                            myDict['目前在使用的银行产品'] = Ans

                        # 第十五题
                        list = [sheet.cell(76, 0).ctype, sheet.cell(77, 0).ctype, sheet.cell(78, 0).ctype,
                                sheet.cell(79, 0).ctype, sheet.cell(80, 0).ctype]
                        if list.count(1) > 1:
                            myDict['平时生活消费的透支支付选择'] = '单选题多选'
                        elif list.count(1) == 0:
                            myDict['平时生活消费的透支支付选择'] = '未填写'
                        else:
                            index = list.index(1) + 76
                            myDict['平时生活消费的透支支付选择'] = sheet.cell_value(index, 2)
                        list.clear()

                        # 第十六题
                        list = [sheet.cell(82, 0).ctype, sheet.cell(83, 0).ctype, sheet.cell(84, 0).ctype,
                                sheet.cell(85, 0).ctype]
                        if list.count(1) > 1:
                            myDict['转账给别人的主要方式'] = '单选题多选'
                        elif list.count(1) == 0:
                            myDict['转账给别人的主要方式'] = '未填写'
                        else:
                            index = list.index(1) + 82
                            myDict['转账给别人的主要方式'] = sheet.cell_value(index, 2)
                        list.clear()

                        # 第十七题（多选）
                        if sheet.cell(87, 0).ctype == 1:
                            a = "银行网站或者电话客服, "
                            ea=ea+1
                        else:
                            a = ""
                        if sheet.cell(88, 0).ctype == 1:
                            b = "银行网点面对面, "
                            eb=eb+1
                        else:
                            b = ""
                        if sheet.cell(89, 0).ctype == 1:
                            c = "朋友圈传播的产品介绍, "
                            ec=ec+1
                        else:
                            c = ""
                        if sheet.cell(90, 0).ctype == 1:
                            d = "手机银行APP, "
                            ed=ed+1
                        else:
                            d = ""
                        if sheet.cell(91, 0).ctype == 1:
                            e = "无贷款需求, "
                            ee=ee+1
                        else:
                            e = ""
                        if a == "" and b == "" and c == "" and d == "" and e == "":
                            # print(f"若有消费贷款需求，希望了解贷款产品的途径：未填写")
                            myDict['若有消费贷款需求，希望了解贷款产品的途径'] = '未填写'
                        else:
                            # print(f"若有消费贷款需求，希望了解贷款产品的途径：{a+b+c+d+e}")
                            Ans=a + b + c + d + e
                            myDict['若有消费贷款需求，希望了解贷款产品的途径'] = Ans

                        # 第十八题
                        list = [sheet.cell(93, 0).ctype, sheet.cell(94, 0).ctype]
                        if list.count(1) > 1:
                            myDict['假如您没有某家银行的账户，但这家银行给您预估一个信用额度，您随时申请使用，您会考虑使用这个授信额度吗？'] = '单选题多选'
                        elif list.count(1) == 0:
                            myDict['假如您没有某家银行的账户，但这家银行给您预估一个信用额度，您随时申请使用，您会考虑使用这个授信额度吗？'] = '未填写'
                        else:
                            index = list.index(1) + 93
                            myDict['假如您没有某家银行的账户，但这家银行给您预估一个信用额度，您随时申请使用，您会考虑使用这个授信额度吗？'] = sheet.cell_value(index, 2)
                        list.clear()

                        # 第十九题
                        list = [sheet.cell(96, 0).ctype, sheet.cell(97, 0).ctype, sheet.cell(98, 0).ctype,
                                sheet.cell(99, 0).ctype]
                        if list.count(1) > 1:
                            myDict['水电气暖等生活缴费的方式'] = '单选题多选'
                        elif list.count(1) == 0:
                            myDict['水电气暖等生活缴费的方式'] = '未填写'
                        else:
                            index = list.index(1) + 96
                            myDict['水电气暖等生活缴费的方式'] = sheet.cell_value(index, 2)
                        list.clear()

                        # 第二十题
                        if sheet.nrows == 103:
                            # print(f"对银行线上渠道和线下渠道的业务受理、办理及信息发布建的建议：{sheet.cell_value(101,1)}")
                            myDict['对银行线上渠道和线下渠道的业务受理、办理及信息发布建的建议'] = sheet.cell_value(101, 1)
                        # else:
                        # print(f"没有第二十题")


                        df = pd.DataFrame(data=myDict, index=[0])
                        data = df.to_dict('records')

                        client = MongoClient('localhost', 27017)
                        # upload to MongoDB
                        db = client['test2']
                        # print(db)
                        db.Survey.insert_many(data)
    i=i+1

#print(f"count:{count}")
#print(f"男:{male}")
#print(f"女:{female}")
#print(f"未填写性别：{none}")
#print(f"性别多选:{false}")

#使能输入中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

labels='男','多填','女','未填写'
size=[male,false,female,none]
explode=(0,0.1,0,0.1)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您的性别是?')
#plt.savefig('1.jpg')
plt.show()

male_lower_than_twenty = db.Survey.count_documents({'性别':'男','年龄': '20岁及以下'})
#print(male_lower_than_twenty)
female_lower_than_twenty = db.Survey.count_documents({'性别':'女','年龄': '20岁及以下'})
#print(female_lower_than_twenty)
male_twenty_to_thirty = db.Survey.count_documents({'性别':'男','年龄': '20-30岁（含）'})
#print(male_twenty_to_thirty)
female_twenty_to_thirty = db.Survey.count_documents({'性别':'女','年龄': '20-30岁（含）'})
#print(female_twenty_to_thirty)
male_thirty_to_fourty = db.Survey.count_documents({'性别':'男','年龄': '30-40岁（含）'})
#print(male_thirty_to_fourty)
female_thirty_to_fourty = db.Survey.count_documents({'性别':'女','年龄': '30-40岁（含）'})
#print(female_thirty_to_fourty)
male_fourty_to_fifty = db.Survey.count_documents({'性别':'男','年龄': '40-50岁（含）'})
#print(male_fourty_to_fifty)
female_fourty_to_fifty = db.Survey.count_documents({'性别':'女','年龄': '40-50岁（含）'})
#print(female_fourty_to_fifty)
male_fifty_to_sixty = db.Survey.count_documents({'性别':'男','年龄': '50-60岁（含）'})
#print(male_fifty_to_sixty)
female_fifty_to_sixty = db.Survey.count_documents({'性别':'女','年龄': '50-60岁（含）'})
#print(female_fifty_to_sixty)
male_greater_than_sixty = db.Survey.count_documents({'性别':'男','年龄': '60岁及以上'})
#print(male_greater_than_sixty)
female_greater_than_sixty = db.Survey.count_documents({'性别':'女','年龄': '60岁及以上'})
#print(female_greater_than_sixty)
male_empty_age = db.Survey.count_documents({'性别':'男','年龄': '未填写'})
#print(male_empty_age)
female_empty_age = db.Survey.count_documents({'性别':'女','年龄': '未填写'})
#print(female_empty_age)
male_error_age=db.Survey.count_documents({'性别':'男','年龄': '单选题多选'})
#print(male_error_age)
female_error_age=db.Survey.count_documents({'性别':'女','年龄': '单选题多选'})
#print(female_error_age)
Age=('20(含)以下','20-30(含)','30-40(含)','40-50(含)','50-60(含)','60(含)以上','未填写','单选题多选')
male=[male_lower_than_twenty,male_twenty_to_thirty,male_thirty_to_fourty,male_fourty_to_fifty,male_fifty_to_sixty,male_greater_than_sixty,male_empty_age,male_error_age]
female=[female_lower_than_twenty,female_twenty_to_thirty,female_thirty_to_fourty,female_fourty_to_fifty,female_fifty_to_sixty,female_greater_than_sixty,female_empty_age,female_error_age]
bar_width=0.3
index_male = np.arange(len(Age))
index_female = index_male + bar_width
plt.bar(index_male, height=male, width=bar_width, color='b', label='男性')
plt.bar(index_female, height=female, width=bar_width, color='g', label='女性')
plt.legend()
plt.xticks(index_male + bar_width/2, Age)
plt.ylabel('数量') # 纵坐标轴标题
plt.title('年龄段性别分布情况')
plt.xticks(rotation=-15)
#plt.savefig('年龄段性别分布情况.jpg')
plt.show()

lower_than_twenty=db.Survey.count_documents({'年龄': '20岁及以下'})
twenty_to_thirty=db.Survey.count_documents({'年龄': '20-30岁（含）'})
thirty_to_fourty=db.Survey.count_documents({'年龄': '30-40岁（含）'})
fourty_to_fifty=db.Survey.count_documents({'年龄': '40-50岁（含）'})
fifty_to_sixty=db.Survey.count_documents({'年龄': '50-60岁（含）'})
greater_than_sixty=db.Survey.count_documents({'年龄': '60岁及以上'})
empty_age=db.Survey.count_documents({'年龄': '未填写'})
error_age=db.Survey.count_documents({'年龄': '单选题多选'})
labels='20岁及以下','20-30岁（含）','单选题多选','30-40岁（含）','40-50岁（含）','未填写','50-60岁（含）','60岁及以上'
size=[lower_than_twenty,twenty_to_thirty,error_age,thirty_to_fourty,fourty_to_fifty,empty_age,fifty_to_sixty,greater_than_sixty]
explode=(0,0,0.1,0,0,0.1,0,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您当前的年龄阶段是?')
#plt.savefig('2.jpg')
plt.show()

a=db.Survey.count_documents({'学历':'高中及以下'})
b=db.Survey.count_documents({'学历':'专科及本科'})
c=db.Survey.count_documents({'学历':'研究生及以上'})
d=db.Survey.count_documents({'学历':'未填写'})
e=db.Survey.count_documents({'学历':'单选题多选'})
labels='高中及以下','未填写','专科及本科','研究生及以上','单选题多选'
size=[a,d,b,c,e]
explode=(0,0.1,0,0,0.2)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您的学历是？')
#plt.savefig('3.jpg')
plt.show()

less_than_one=db.Survey.count_documents({'每月去网点次数':'不足1次'})
one_to_two=db.Survey.count_documents({'每月去网点次数':'1-2次'})
greater_than_two=db.Survey.count_documents({'每月去网点次数':'2次以上'})
empty_times=db.Survey.count_documents({'每月去网点次数':'未填写'})
error_times=db.Survey.count_documents({'每月去网点次数':'单选题多选'})
labels='不足1次','未填写','1-2次','2次以上','单选题多选'
size=[less_than_one,empty_times,one_to_two,greater_than_two,error_times]
explode=(0,0.1,0,0.1,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您每月去银行网点的次数是?')
#plt.savefig('4.jpg')
plt.show()

less_than_one=db.Survey.count_documents({'最常用的手机银行每月使用次数':'不足1次'})
one_to_two=db.Survey.count_documents({'最常用的手机银行每月使用次数':'1-2次'})
greater_than_two=db.Survey.count_documents({'最常用的手机银行每月使用次数':'2次以上'})
empty_times=db.Survey.count_documents({'最常用的手机银行每月使用次数':'未填写'})
error_times=db.Survey.count_documents({'最常用的手机银行每月使用次数':'单选题多选'})
labels='不足1次','未填写','1-2次','单选题多选','2次以上'
size=[less_than_one,empty_times,one_to_two,error_times,greater_than_two]
explode=(0,0.1,0,0.1,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('针对您最常用的手机银行，每月使用的次数大概是？')
#plt.savefig('5.jpg')
plt.show()

a=db.Survey.count_documents({'日常生活消费常用支付方式':'现金'})
b=db.Survey.count_documents({'日常生活消费常用支付方式':'银行的手机银行APP'})
c=db.Survey.count_documents({'日常生活消费常用支付方式':'微信或支付宝'})
d=db.Survey.count_documents({'日常生活消费常用支付方式':'刷卡'})
e=db.Survey.count_documents({'日常生活消费常用支付方式':'未填写'})
f=db.Survey.count_documents({'日常生活消费常用支付方式':'单选题多选'})
labels='现金','未填写','银行的手机银行APP','微信或支付宝','单选题多选','刷卡'
size=[a,e,b,c,f,d]
explode=(0,0.1,0,0,0.1,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您日常生活消费时常用的支付方式是？')
#plt.savefig('6.jpg')
plt.show()

a=db.Survey.count_documents({'常用方式查询银行账户余额':'公众号'})
b=db.Survey.count_documents({'常用方式查询银行账户余额':'手机银行'})
c=db.Survey.count_documents({'常用方式查询银行账户余额':'ATM'})
d=db.Survey.count_documents({'常用方式查询银行账户余额':'柜面'})
e=db.Survey.count_documents({'常用方式查询银行账户余额':'客服电话'})
f=db.Survey.count_documents({'常用方式查询银行账户余额':'未填写'})
g=db.Survey.count_documents({'常用方式查询银行账户余额':'单选题多选'})
labels='公众号','手机银行','未填写','ATM','单选题多选','客服电话','柜面'
size=[a,b,f,c,g,e,d]
explode=(0.1,0,0.1,0,0,0.1,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('你最常用哪种方式查询银行账户余额？')
#plt.savefig('7.jpg')
plt.show()

a=db.Survey.count_documents({'最常用办理银行业务的方式':'寻找周边的ATM'})
b=db.Survey.count_documents({'最常用办理银行业务的方式':'利用银行公众号或者小程序'})
c=db.Survey.count_documents({'最常用办理银行业务的方式':'去银行网点的柜面办理'})
d=db.Survey.count_documents({'最常用办理银行业务的方式':'利用银行的手机银行或网上银行'})
e=db.Survey.count_documents({'最常用办理银行业务的方式':'未填写'})
f=db.Survey.count_documents({'最常用办理银行业务的方式':'单选题多选'})
labels='寻找周边的ATM','未填写','利用银行公众号或者小程序','去银行网点的柜面办理','单选题多选','利用银行的手机银行或网上银行'
size=[a,e,b,c,f,d]
explode=(0,0.1,0,0,0.1,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您回想下需要办理银行业务时，最常用的方式是？')
#plt.savefig('8.jpg')
plt.show()

a=db.Survey.count_documents({'银行网点使用最多的业务':'ATM等自助设备'})
b=db.Survey.count_documents({'银行网点使用最多的业务':'柜面办理'})
c=db.Survey.count_documents({'银行网点使用最多的业务':'直接找贵宾服务'})
d=db.Survey.count_documents({'银行网点使用最多的业务':'大堂客户经理辅助使用的移动便携设备'})
e=db.Survey.count_documents({'银行网点使用最多的业务':'未填写'})
f=db.Survey.count_documents({'银行网点使用最多的业务':'单选题多选'})
labels='ATM等自助设备','未填写','柜面办理','直接找贵宾服务','单选题多选','大堂客户经理辅助使用的移动便携设备'
size=[a,e,b,c,f,d]
explode=(0,0.1,0,0,0.1,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您到银行网点办理业务时，使用最多的是？')
#plt.savefig('9.jpg')
plt.show()

# print(aa)
# print(ab)
# print(ac)
# print(ad)
# print(ae)
# print(af)
# print(ag)

empty_Question_ten=db.Survey.count_documents({'登录某家银行的手机银行APP一般使用的功能':'未填写'})
Question_ten = ('A', 'B', 'C', 'D', 'E','F','G','未填写')
number = [aa, ab, ac, ad, ae,af,ag,empty_Question_ten]
plt.bar(Question_ten, number)
plt.title('您登录使用某家银行的手机银行APP时，一般使用那些功能？（可多选）')
#plt.savefig('10.jpg')
plt.show()

empty_Question_eleven=db.Survey.count_documents({'选择银行服务时更看重的渠道':'未填写'})
Question_eleven = ('A', 'B', 'C', 'D','未填写')
number = [ba, bb, bc, bd,empty_Question_eleven]
plt.bar(Question_eleven, number)
plt.title('选择银行服务时，您更看重银行服务的那些渠道？（可多选）')
#plt.savefig('11.jpg')
plt.show()

empty_Question_twelve=db.Survey.count_documents({'登录某家银行的手机银行APP一般使用的功能':'未填写'})
Question_twelve = ('A', 'B', 'C', 'D', 'E', '未填写')
number = [ca, cb, cc, cd, ce, empty_Question_eleven]
plt.bar(Question_twelve, number)
plt.title('您希望在哪个渠道参与并享受到银行的优惠促销活动？（可多选）')
#plt.savefig('12.jpg')
plt.show()

a=db.Survey.count_documents({'选择银行的业务办理渠道的原因':'线上办理省时省力，即使附近有网点也不愿去'})
b=db.Survey.count_documents({'选择银行的业务办理渠道的原因':'因为没时间去网点，只能选择线上办理'})
c=db.Survey.count_documents({'选择银行的业务办理渠道的原因':'专属客户经理通过电话、微信等线上沟通推荐后，再去网点办理，这样既安全又能享受专属服务'})
d=db.Survey.count_documents({'选择银行的业务办理渠道的原因':'直接去网点办理，享受面对面服务'})
e=db.Survey.count_documents({'选择银行的业务办理渠道的原因':'未填写'})
f=db.Survey.count_documents({'选择银行的业务办理渠道的原因':'单选题多选'})
labels='A','未填写','B','C','单选题多选','D'
size=[a,e,b,c,f,d]
explode=(0,0.1,0,0,0.1,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您选择银行的业务办理渠道时，哪个更符合您的现状？')
#plt.savefig('13.jpg')
plt.show()

Question_fourteen = ('A', 'B', 'C', 'D', 'E')
number = [da, dg, dc, dd, de]
plt.bar(Question_fourteen, number)
plt.title('您目前在使用的银行产品有？（可多选）')
#plt.savefig('14.jpg')
plt.show()

a=db.Survey.count_documents({'平时生活消费的透支支付选择':'花呗'})
b=db.Survey.count_documents({'平时生活消费的透支支付选择':'白条'})
c=db.Survey.count_documents({'平时生活消费的透支支付选择':'线下刷信用卡'})
d=db.Survey.count_documents({'平时生活消费的透支支付选择':'微信支付宝绑定信用卡'})
e=db.Survey.count_documents({'平时生活消费的透支支付选择':'不使用透支支付'})
f=db.Survey.count_documents({'平时生活消费的透支支付选择':'未填写'})
g=db.Survey.count_documents({'平时生活消费的透支支付选择':'单选题多选'})
labels='A','B','C','单选题多选','D','未填写','E'
size=[a,b,c,g,d,f,e]
explode=(0,0.1,0,0,0.1,0,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您在平时生活消费的透支支付时，使用最多的是？')
#plt.savefig('15.jpg')
plt.show()

a=db.Survey.count_documents({'转账给别人的主要方式':'ATM等自助设备'})
b=db.Survey.count_documents({'转账给别人的主要方式':'柜面'})
c=db.Survey.count_documents({'转账给别人的主要方式':'手机银行或者网上银行'})
d=db.Survey.count_documents({'转账给别人的主要方式':'请别人代转账'})
e=db.Survey.count_documents({'转账给别人的主要方式':'未填写'})
f=db.Survey.count_documents({'转账给别人的主要方式':'单选题多选'})
labels='A','未填写','B','C','D','单选题多选'
size=[a,e,b,c,d,f]
explode=(0,0.1,0,0,0.1,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您选择银行的业务办理渠道时，哪个更符合您的现状？')
#plt.savefig('16.jpg')
plt.show()

Question_seventeen = ('A', 'B', 'C', 'D', 'E')
number = [ea, eb, ec, ed, ee]
plt.bar(Question_seventeen, number)
plt.title('若有消费贷款需求，您想通过什么途径了解贷款产品?（可多选）')
#plt.savefig('17.jpg')
plt.show()

a=db.Survey.count_documents({'假如您没有某家银行的账户，但这家银行给您预估一个信用额度，您随时申请使用，您会考虑使用这个授信额度吗？':'会'})
b=db.Survey.count_documents({'假如您没有某家银行的账户，但这家银行给您预估一个信用额度，您随时申请使用，您会考虑使用这个授信额度吗？':'不会'})
c=db.Survey.count_documents({'假如您没有某家银行的账户，但这家银行给您预估一个信用额度，您随时申请使用，您会考虑使用这个授信额度吗？':'未填写'})
d=db.Survey.count_documents({'假如您没有某家银行的账户，但这家银行给您预估一个信用额度，您随时申请使用，您会考虑使用这个授信额度吗？':'单选题多选'})
labels='未填写','A','单选题多选','B'
size=[c,a,d,b]
explode=(0,0,0,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('假如您没有某家银行的账户，但这家银行给您预估一个信用额度，\n您随时申请使用，您会考虑使用这个授信额度吗？')
#plt.savefig('18.jpg')
plt.show()

a=db.Survey.count_documents({'水电气暖等生活缴费的方式':'银行的手机银行'})
b=db.Survey.count_documents({'水电气暖等生活缴费的方式':'支付宝或微信钱包'})
c=db.Survey.count_documents({'水电气暖等生活缴费的方式':'公众号'})
d=db.Survey.count_documents({'水电气暖等生活缴费的方式':'分别去水电气暖公司或者物业缴纳'})
e=db.Survey.count_documents({'水电气暖等生活缴费的方式':'未填写'})
f=db.Survey.count_documents({'水电气暖等生活缴费的方式':'单选题多选'})
labels='A','未填写','B','C','D','单选题多选'
size=[a,e,b,c,d,f]
explode=(0,0.1,0,0,0.1,0)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('您家的水电气暖等生活缴费，您会选择哪种缴费方式？')
#plt.savefig('19.jpg')
plt.show()

AA = db.Survey.count_documents({'性别':'男','每月去网点次数':'不足1次'})
BA = db.Survey.count_documents({'性别':'女','每月去网点次数':'不足1次'})
AB = db.Survey.count_documents({'性别':'男','每月去网点次数':'1-2次'})
BB = db.Survey.count_documents({'性别':'女','每月去网点次数':'1-2次'})
AC = db.Survey.count_documents({'性别':'男','每月去网点次数':'2次以上'})
BC = db.Survey.count_documents({'性别':'女','每月去网点次数':'2次以上'})
Times=('不足1次','1-2次','2次以上')
male=[AA,AB,AC]
female=[BA,BB,BC]
bar_width=0.3
index_male = np.arange(len(Times))
index_female = index_male + bar_width
plt.bar(index_male, height=male, width=bar_width, color='b', label='男性')
plt.bar(index_female, height=female, width=bar_width, color='g', label='女性')
plt.legend()
plt.xticks(index_male + bar_width/2, Times)
plt.ylabel('数量') # 纵坐标轴标题
plt.title('每月去银行网点次数性别分布情况')
plt.xticks(rotation=-15)
#plt.savefig('每月去银行网点次数性别分布情况.jpg')
plt.show()

AA = db.Survey.count_documents({'学历':'高中及以下','每月去网点次数':'不足1次'})
BA = db.Survey.count_documents({'学历':'专科及本科','每月去网点次数':'不足1次'})
CA = db.Survey.count_documents({'学历':'研究生及以上','每月去网点次数':'不足1次'})
AB = db.Survey.count_documents({'学历':'高中及以下','每月去网点次数':'1-2次'})
BB = db.Survey.count_documents({'学历':'专科及本科','每月去网点次数':'1-2次'})
CB = db.Survey.count_documents({'学历':'研究生及以上','每月去网点次数':'1-2次'})
AC = db.Survey.count_documents({'学历':'高中及以下','每月去网点次数':'2次以上'})
BC = db.Survey.count_documents({'学历':'专科及本科','每月去网点次数':'2次以上'})
CC = db.Survey.count_documents({'学历':'研究生及以上','每月去网点次数':'2次以上'})
Times=('不足1次','1-2次','2次以上')
AAA=[AA,AB,AC]
BBB=[BA,BB,BC]
CCC=[CA,CB,CC]
bar_width=0.3
index_AAA = np.arange(len(Times))
index_BBB = index_AAA + bar_width
index_CCC = index_BBB + bar_width
plt.bar(index_AAA, height=AAA, width=bar_width, color='b', label='高中及以下')
plt.bar(index_BBB, height=BBB, width=bar_width, color='g', label='专科及本科')
plt.bar(index_CCC, height=CCC, width=bar_width, color='r', label='研究生及以上')
plt.legend()
plt.xticks(index_AAA + bar_width/2, Times)
plt.ylabel('数量') # 纵坐标轴标题
plt.title('每月去银行网点次数学历分布情况')
plt.xticks(rotation=-15)
#plt.savefig('每月去银行网点次数学历分布情况.jpg')
plt.show()

AA = db.Survey.count_documents({'年龄': '20岁及以下','每月去网点次数':'不足1次'})
BA = db.Survey.count_documents({'年龄': '20-30岁（含）','每月去网点次数':'不足1次'})
CA = db.Survey.count_documents({'年龄': '30-40岁（含）','每月去网点次数':'不足1次'})
DA = db.Survey.count_documents({'年龄': '40-50岁（含）','每月去网点次数':'不足1次'})
EA = db.Survey.count_documents({'年龄': '50-60岁（含）','每月去网点次数':'不足1次'})
FA = db.Survey.count_documents({'年龄': '60岁及以上','每月去网点次数':'不足1次'})
AB = db.Survey.count_documents({'年龄': '20岁及以下','每月去网点次数':'1-2次'})
BB = db.Survey.count_documents({'年龄': '20-30岁（含）','每月去网点次数':'1-2次'})
CB = db.Survey.count_documents({'年龄': '30-40岁（含）','每月去网点次数':'1-2次'})
DB = db.Survey.count_documents({'年龄': '40-50岁（含）','每月去网点次数':'1-2次'})
EB = db.Survey.count_documents({'年龄': '50-60岁（含）','每月去网点次数':'1-2次'})
FB = db.Survey.count_documents({'年龄': '60岁及以上','每月去网点次数':'1-2次'})
AC = db.Survey.count_documents({'年龄': '20岁及以下','每月去网点次数':'2次以上'})
BC = db.Survey.count_documents({'年龄': '20-30岁（含）','每月去网点次数':'2次以上'})
CC = db.Survey.count_documents({'年龄': '30-40岁（含）','每月去网点次数':'2次以上'})
DC = db.Survey.count_documents({'年龄': '40-50岁（含）','每月去网点次数':'2次以上'})
EC = db.Survey.count_documents({'年龄': '50-60岁（含）','每月去网点次数':'2次以上'})
FC = db.Survey.count_documents({'年龄': '60岁及以上','每月去网点次数':'2次以上'})
Times=('不足1次','1-2次','2次以上')
AAA=[AA,AB,AC]
BBB=[BA,BB,BC]
CCC=[CA,CB,CC]
DDD=[DA,DB,DC]
EEE=[EA,EB,EC]
FFF=[FA,FB,FC]
bar_width=0.1
index_AAA = np.arange(len(Times))
index_BBB = index_AAA + bar_width
index_CCC = index_BBB + bar_width
index_DDD = index_CCC + bar_width
index_EEE = index_DDD + bar_width
index_FFF = index_EEE + bar_width
plt.bar(index_AAA, height=AAA, width=bar_width, color='b', label='20岁及以下')
plt.bar(index_BBB, height=BBB, width=bar_width, color='g', label='20-30岁（含）')
plt.bar(index_CCC, height=CCC, width=bar_width, color='r', label='30-40岁（含）')
plt.bar(index_DDD, height=DDD, width=bar_width, color='c', label='40-50岁（含）')
plt.bar(index_EEE, height=EEE, width=bar_width, color='m', label='50-60岁（含）')
plt.bar(index_FFF, height=FFF, width=bar_width, color='y', label='60岁及以上')
plt.legend()
plt.xticks(index_CCC + bar_width/2, Times)
plt.ylabel('数量') # 纵坐标轴标题
plt.title('每月去银行网点次数年龄分布情况')
plt.xticks(rotation=-15)
#plt.savefig('每月去银行网点次数年龄分布情况.jpg')
plt.show()

# data = pd.read_csv("C://Users//dell//Desktop//Survey.csv")
# data.head()
# data_x = data['年龄']
# data_y = data['性别']
# from sklearn.model_selection import train_test_split
# train_x, valid_x, train_y, valid_y = train_test_split(data_x, data_y, test_size=0.33, random_state = 1)
# import matplotlib.pyplot as plt
# plt.scatter(train_x, train_y, facecolor='None', edgecolor='k', alpha=0.3)
# plt.show()
# data.describe()
# plt.scatter(data_x,data_y)
# yhat = 0.0017 * data_x + 0.275
# fig = plt.plot(data_x, yhat, lw=4, color='c',label = 'regressionline')
# plt.xlabel(data_x, fontsize = 20)
# plt.ylabel(data_y, fontsize = 20)
# plt.show()
