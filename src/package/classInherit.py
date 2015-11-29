'''
Created on 2015年9月1日

@author: Administrator
'''

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position
    def feek(self,info):
        print('make noise '+info)
    def go(self,way,info):
         print('go way '+way)
         self.feek(info)
         
         
class happyBird(Bird):
    def __init__(self,bool1,way):
        have_feather=bool1
        way_of_reproduction=way