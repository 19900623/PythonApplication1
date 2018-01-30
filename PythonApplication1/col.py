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
         pass
          #print("********")

   #def __init__(self, sheng, shi, qu, xuexiao):
	  #self.qu = qu
	  #self.xuexiao = xuexiao
	  #self.sheng = sheng
	  #self.shi = shi
   #   #Employee.empCount += 1
 
     def pCol(self):
         print ("省 : ", self.sheng,  ", 市: ", self.shi,  ", 区: ", self.qu)
