'''
Created on 2015年9月5日

@author: Administrator
'''
# S = 'abcdefghijk'
# for i in range(0,len(S),2):
#     print (S[i])
#     
# S = 'abcdefghijk'
# for (a,b) in enumerate(S):
#     print(a,b)  
#     
#     
# ta=range(1,4,1)
# tb=range(10,17,3)
# tc=("aaa",'bbb','ccc')
# for(ta,tb,tc) in zip(ta,tb,tc):
#     print(ta,tb,tc)
#     
#     
# ta = [1,2,3]
# tb = [9,8,7]
# 
# # cluster
# zipped = zip(ta,tb)
# print(zipped)
# 
# na, nb = zip(*zipped)
# print(na, nb)




# def gen():
#     a = 100
#     yield a
#     a = a*8
#     yield a
#     yield 1000
#     
# for i in gen():
#     print (i)
#     
#     
# G = (x for x in range(4))
# print(G)
# print(type(G))
# for a in G:
#     print(a)
    
# L = []
# for x in range(10):
#     L.append(x**2)
# print(L)
# print(type(L))
# for a in L:
#     print(a)
# 
# L = [x**2 for x in range(10)]
# print(type(L))
# for a in L:
#     print(a)
    
re=reduce((lambda x,y:x+y),{1,2,3,4,5,6})
print(type(re))
print(re)
