#冒泡，选择，插入，快排，二分，
def maopao(arr):
    for i in range(len(arr)-1, 0 , -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr



#选择
def xuanze(arr):
    for i in range(len(arr)):
        minData = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minData]:
                i = j

        if arr[i] < arr[minData]:
            tmp = arr[i]
            arr[i] = arr[minData]
            arr[minData] = tmp  
    return arr


#插入
def charu(arr):
    for i in range(1,len(arr)):
        nowData = arr[i]
        position = i
        while arr[position-1] > nowData:
            arr[position] = arr[position-1] 
            position = position-1
        arr[position] =  nowData
    return arr

#快排
def kuaipai(arr):
    if len(arr) <= 1:
        return arr
    minData = arr[0]
    arr1 = []
    arr2 = []
    for i in range(1, len(arr)):
        if arr[i] <= minData:
            arr1.append(arr[i])
        if arr[i] > minData:
            arr2.append(arr[i])
    
    arr1 = kuaipai(arr1)
    arr2 = kuaipai(arr2)
    return arr1+[minData]+arr2

arr = [1,3,2,4,5,9,8,7,10,6]
arr = kuaipai(arr)
print(arr)
