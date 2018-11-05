#顺序表查找，最基本的查找，对数据进行遍历
def search(arr, item):
    pos = 0
    while pos < len(arr):
        if arr[pos] == item:
            return pos
        pos+=1

arr = [1, 2, 3, 6, 43, 23, 66]
location = search(arr, 6)
print(location)
