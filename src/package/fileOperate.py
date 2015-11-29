'''
Created on 2015年8月31日

@author: Administrator
'''
class fileOperator(object):
    path='C:\\Users\\Administrator\\Desktop\\text.txt'
    instancePara='局部变量'
    def descript(self):
        print(self.instancePara)
        
    def writetxt(text):
        f=open(fileOperator.path,'w')
        f.write(text)
        f.close
        
    def output():
        f=open(fileOperator.path,'r')
        content=f.read();
        f.close
        print(content)
        
    def addText(text):
        f=open(fileOperator.path,'a')
        f.write(text)
        f.close



