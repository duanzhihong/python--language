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
test = (200, 50)
for value in test:
    print(value)