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
import json

#from pandas import Sereis, DataFrame

# Connect to the database

config = {
          'host':'192.168.67.188',
          'port':3306,
          'user':'sa',
          'password':'1234',
          'db':'maodb',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }



class Col(object):
     def __init__(self):
         pass

     def pCol(self):
         print("省 : ", self.sheng,"省id : ", self.shengid,  ", 市: ", self.shi,  ", 市id: ", self.shiid,  ", 区: ", self.qu, ", 区id: ", self.quid,"学校:",self.xuexiao)

class mysqlCol(object):
     def __init__(self):
         pass

     def pCol(self):
         print("省 : ", self.shengid,  ", 市: ", self.shiid,  ", 区: " ,self.quid, ", 名字: ", self.areaName)

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

#--------------------------------------
#for i in range(len(arr2)):
#	#print (arr[i])
#	#c.pCol()
#	for j in range(len(arr2[i])):
#		if j==0:
#			print(arr2[i][j])
#		elif j==1:
#			print(arr2[i][j])
#--------------------------------------





#for x in colArray:
    #print(x.sheng,x.shi,x.qu,x.xuexiao)





class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(obj, date):  
            return obj.strftime("%Y-%m-%d")  
        else:  
            return json.JSONEncoder.default(self, obj) 


# Connect to the database
connection = pymysql.connect(**config)

# 获取雇佣日期
#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(2018, 12, 31)

# 执行sql语句
def ping(self, reconnect=True):
        """Check if the server is alive"""
        if self._sock is None:
            if reconnect:
                self.connect()
                reconnect = False
            else:
                raise err.Error("Already closed")
        try:
            self._execute_command(COMMAND.COM_PING, "")
            return self._read_ok_packet()
        except Exception:
            if reconnect:
                self.connect()
                return self.ping(False)
            else:
                raise
def reConnect(self):
    try:
        self.connection.ping()
    except:
        self.connection()

def getNumber( name ):
    "这是函数"
    global in_json
    global arr_print
    arr_print=[]
    try:
        connection.ping()
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "SELECT * FROM base_area where AreaName='{}' ".format(name)
            cursor.execute(sql)
            # 获取查询结果
            result = cursor.fetchall()
        
            for row in result:
                #r = json.dumps(row, cls=DateEncoder)  
                #r2 = json.loads(r);
                areaId=row["AreaId"]
                areaName=row["AreaName"]
                o =  mysqlCol()
                o.areaId=areaId
                o.areaName=areaName
                print(areaId)
                print(areaName)
                print(name)
                arr_print.append(o)
            #in_json = json.dumps(result) 
            #print(result)
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
        print(arr_print)
    finally:
        connection.close();
    if arr_print:
        return arr_print
        pass
    else:
        o =  mysqlCol()
        o.areaId="1"
        o.areaName="1"
        arr_print.append(o)
        return arr_print
        pass
    




global text
global colArray 
colArray=[]
for i in range(len(arr)):
	#print (arr[i])
	#print('************')
	c = Col()
	for j in range(len(arr[i])):
	   #print(arr[i][j])
	   text = arr[i][j]
	   if j==0:
	       c.sheng = text
	       temp=[]
	       temp = getNumber(text)
	       c.shengid=temp[0].areaId
	   elif j==1:
	       c.shi = text
	       temp=[]
	       temp = getNumber(text)
	       c.shiid=temp[0].areaId
	   elif j==2:
	       c.qu = text
	       temp=[]
	       temp = getNumber(text)
	       c.quid=temp[0].areaId
	   elif j==3:
	       c.xuexiao = text
	#c.pCol()
	colArray.append(c)






#---------------------------------
for x in colArray:
    print("INSERT Base_Organize (CreationTime,IsDeleted,OrganizeId,ParentId,EnCode,ShortName,FullName,Nature,ProvinceId,CityId,CountyId,WebAddress,FoundedTime,Layer,SortCode,DeleteMark,EnabledMark) VALUES ('2017-11-14 08:25:44',0, '279348e8-0385-4564-ad31-9684d3355d46','4d721184-9778-4b52-ae74-96de7efcd59c','','','{}','其他业','{}','{}','{}','','2013-06-06 00:00:00',1,1,0,1);".format(x.xuexiao,x.shengid,x.shiid,x.quid))



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
