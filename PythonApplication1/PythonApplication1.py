# -*- coding: UTF-8 -*-

# Filename : helloworld.py
# author by : www.runoob.com

# 该实例输出 Hello World!
#print('Hello World!')
# pip install pandas

#easy_install xlrd

#pip install MySQL-python

#mysql报错
#pip install pyMysql
import pandas as pd
import csv
import pymysql.cursors
import datetime

#from pandas import Sereis, DataFrame

# Connect to the database

#config = {
#          'host':'192.168.67.188',
#          'port':3306,
#          'user':'sa',
#          'password':'1234',
#          'db':'maodb',
#          'charset':'utf8mb4',
#          'cursorclass':pymysql.cursors.DictCursor,
#          }

## Connect to the database
#connection = pymysql.connect(**config)

## 获取雇佣日期
#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(2018, 12, 31)

## 执行sql语句
#try:
#    with connection.cursor() as cursor:
#        # 执行sql语句，进行查询
#        sql = 'SELECT * FROM base_area '
#        cursor.execute(sql)
#        # 获取查询结果
#        result = cursor.fetchone()
#        print(result)
#    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
#    connection.commit()
 
#finally:
#    connection.close();
#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Col(object):
   #'行基类'
   #empCount = 0
 
   #def __init__(self,name,gender,birth,**kw):
   #     self.name=name
   #     self.gender=gender
   #     self.birth=birth
   #     for k,w in kw.iteritems():
			#setattr(self,k,w)
     def __init__(self):
          print("Instance Created")

   #def __init__(self, sheng, shi, qu, xuexiao):
	  #self.qu = qu
	  #self.xuexiao = xuexiao
	  #self.sheng = sheng
	  #self.shi = shi
   #   #Employee.empCount += 1
 
     def pCol(self):
         print("省 : ", self.sheng,  ", 市: ", self.shi,  ", 区: ", self.qu,"学校:",self.xuexiao)


#取哪行
list = [0,1,2,3,5]
np = pd.read_csv('school.csv',index_col=0,usecols=list)

area = pd.read_csv('base_area1.csv',index_col=0,usecols=[0,1,4])

#print(area)
#data =
#DataFrame(np.arange(16).reshape(4,4),index=list('abcd'),columns=list('wxyz'))
#ser = Series(np.arange(3.))

#print(np.values)
arr = np.values
arr2 = area.values
#sql=df.to_csv('school.csv',index=False,encoding='utf-8')
sql_list = []
#for i in df:
#    #i.append(sql_list)
#    print(i)

#print (df)
#print (df[0:])
#print (df.dtypes)
i = 0
#data = df[0:]
#global text
print(area.values)
for i in range(len(arr2)):
	#print (arr[i])
	#c.pCol()
	for j in range(len(arr2[i])):
		if j==0:
			print(arr2[i][j])
		elif j==1:
			print(arr2[i][j])
	#print('************')
#global text
#for i in range(len(arr)):
#	#print (arr[i])
#	print('************')
#	c = Col()
#	#c.pCol()
#	for j in range(len(arr[i])):
#	   #print(arr[i][j])
	   
#	   text = arr[i][j]
#	   if j==0:
#	       c.sheng = text
#	   elif j==1:
#	       c.shi = text
#	   elif j==2:
#	       c.qu = text
#	   elif j==3:
#	       c.xuexiao = text
#	c.pCol()


















    #data.append(list(line.strip().split(',')))
	#print('行:',i)
	#col=data[index:index+1]
	
	#print()

	
    #print ("行:",index)
    #print (df[index])
    #i+=1

#for x in data:
#    #if x==0:
#         print(i)
#         print(x)
#    #else:
#    #    pass
#         i+=1



#class Area(object):
#    '''
#    地区
#    '''
#    pass

#class  County(object):
#    '''
#    县
#    '''
#    pass

#class Town(object):
#    '''
#    城镇
#    '''
#    pass
