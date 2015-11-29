'''
Created on 2015年9月5日

@author: Administrator
'''


import os.path
from sys import path
path='C:/Users/Administrator/Desktop/text.txt'

print(os.path.basename(path))    # 查询路径中包含的文件名
print(os.path.dirname(path))     # 查询路径中包含的目录

info = os.path.split(path)       # 将路径分割成文件名和目录两个部分，放在一个表中返回
print(type(info))

print(info[0])

print(os.path.exists(path))    # 查询文件是否存在

print(os.path.getsize(path))   # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间

print(os.path.isfile(path))    # 路径是否指向常规文件
print(os.path.isdir(path))     # 路径是否指向目录文件
    # 路径是否指向目录文件

# print(os.listdir('C:/Users/Administrator/Desktop/'))


import glob
# list=glob.glob('C:/Users/Administrator/Desktop/*')
# for a in list:
#     print(a)

# path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt')  # 使用目录名和文件名构成一个路径字符串
# 
# p_list = [path, path2]
# print(p_list)
# print(os.path.commonprefix(p_list))    # 查询多个路径的共同部分

filelist=[]
 
def getAllFile(path,filelist):
    if(os.path.exists(path)==False):
        print("此文件或路徑不存在")
        return
    list=glob.glob(path+'/*')
    for a in list:
        if(os.path.isdir(a)):
            getAllFile(a,filelist)
        if(os.path.isfile(a)):
            filelist.append(a)
         
getAllFile('C:/Users/Administrator/Desktop',filelist)

for file in filelist:
    print(file)
    
