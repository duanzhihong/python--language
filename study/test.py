# print("hello world")
# name = "duan zhi hong"
# print(name.title())
#全部转化为大小写 upper() lower()
#除去末尾的空格
# language = 'duan '
# print(language.rstrip())
# age = 23
#str函数，表示为字符串
# print("nihao" + str(age) + 'ma')
# print(3/2);
#list数据类型 访问-1返回的是最后的一个元素
# test = ['1', '2', 'duan']
# print(test[-1].title());
# test.append("nihao") append在列表中添加元素
# test.insert(1,'jh') insert在索引为x的位置添加数据
# print(test)
# del test[0] del删除一个元素
# print(test)
#a = test.pop() pop删除末尾的元素并且返回值，可以将列表看成一个栈 指定一个索引，可以删除固定的数据
# print(a)
#test.remove('duan') remove 通过固定的值进行删除
# print(test)
# sort()将列表进行升序排序,降序的话传递参数reverse = true 会永久修改列表的数据
# sorted() 不会永久修改列表的数据
# test = ['alice', 'david', 'carolina']
# for elem in test:
#     print(elem)
# print('end')
# for a in range(1,4):
    # print(a)
# a = list(range(2, 11, 2)) 
# print(a)
#创建十个数的平方
# test = []
# for value in range(1, 11):
#     data = value**2
#     test.append(data)
# print(test)
# digits = [1, 2, 3, 6]
# print(max(digits))
# print(min(digits))
# print(sum(digits))
#列表解析
# test = [value**2 for value in range(1,11)]
# print(test)
# player = ['duan', 'zhi', 'hong', 'ni', 'hao']
# print(player[0:2]) 对列表进行切片，类似于将数组切割 
#复制列表
# my_foods = ['duan', 'zhi', 'hong']
# his_foods = my_foods[:]
# print(his_foods)
#元组 其中的数据是不可以更改的
# test = (200, 50)
# for value in test:
#     print(value)
# if语句
# cars = ['audi', 'bmw', 'subrau', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper()) #所有文字大写
#     else:
#         print(car.title()) #首文字大写
# banner_users = ['duan', 'zhi', 'hong']
# if 'nam' not in banner_users:
#     print('nihao')
# test = ('duan', 'zhi', 'hong')
# if 'no' not in test:
#     print('oo')
# 字典 类似与php中的关联数组
# alien_0 = {'color':'green', 'points':5}
# print(alien_0['color'])
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 3
# alien_0['points'] = 6
# del alien_0['points'] #删除键
# print(alien_0)
#遍历字典
# user_0 = {
#     'username': 'a',
#     'first': 'b',
#     'last': 'c',
#     'no': 'b'
# }
#遍历所有数据
# for key, value in user_0.items():
#     print(value)
# #遍历键名
# for key in user_0.keys():
#     print(key)
#sort将键名 进行排序后再输出
# for key in sorted(user_0.keys()):
#     print(key)
# 遍历键值
# for value in user_0.values():
#     print(value)
# for value in set(user_0.values()): #set无序集合
#     print(value)
# for value in range(5):
#     print(value)

#用户输入
# message = input('your name')
# print('hello'+message)
# age = input('how old are you?')
# print(age)

#求模运算(取余)
# print(5%3)

# current = 1
# while(current < 5):
#     print(current)
#     current+=1

# pets = ['cat', 'cat', 'cat', 'duan', 'zhi', 'dog']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

#基本的函数
# def greet_user():
    # print("hello world")
# greet_user()

#模版引入
#使用方法 module_name.function_name()
# import test2
# test2.test()
#from  module_name import function_name()
# from test2 import test as te
#form module_name import function_name1(), function_name2()
# te()
#使用as来给函数起别名

# 创建类的基本使用
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(self.name.title()+'sit')
#     def roll(self):
#         print(self.name.title()+'roll')
# dog = Dog('gou',18)
# dog.sit()
# dog.roll()

#类的继承 类似php继承，记得形参中添加self
# class BigDog(Dog):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def big(self):
#         print('this is big dog')

# bigDog = BigDog('gou', 33)
# bigDog.sit()
# bigDog.roll()
# bigDog.big()

#getitem setitem
# class test():
#     def __init__(self):
#         pass
#     def __getitem__(self, key):
#         return 'nonono'
#     def __setitem__(self, key, data):
#         self.key = data
#         print('setitem')
#         return 'add success'

# test = test()
# test[2] = 'duan'
# print(test[2])

#打开文件
# with open('pi.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# test = range(5, 0, -1)
# for value in test:
#     print(value)
# test2 = range(5)
# for value in test2:
#     print(value)

#遍历行
# filename = 'pi.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

#保存内容在with之外使用
filename = 'pi.txt'
with open(filename) as file_object:
        lines = file_object.readlines()
# print(lines)
# for line in lines:
#     print(line.rstrip())
pi = lines[0]
# print(pi)
string = ''
for value in pi:
    # if not value.isspace():
        string += value.strip()

print(string)
