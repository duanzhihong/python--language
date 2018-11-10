#快排
def kuaipai(arr):
    if len(arr) == 0:
        return []
    tmp = arr[0]
    minArr = []
    maxArr = []
    for i in range(1,len(arr)):
        if tmp < arr[i]:
            minArr.append(arr[i])
        if tmp > arr[i]:
            maxArr.append(arr[i])
    minArr = kuaipai(minArr)
    maxArr = kuaipai(maxArr)
    return minArr+[tmp]+maxArr

arr = [12, 11, 34, 13, 35, 87,1]
arr = kuaipai(arr)
print(arr)