#桶排序
def bucketSort(arr):
    newArr = [0]*len(arr)
    # print(newArr)
    result =[]
    for i in range(len(arr)):
        newArr[arr[i]] += 1
    for j in range(len(arr)):
        result += [j]*newArr[j]
    print(result)
arr = [5,3,6,1,2,7,5,4]
bucketSort(arr)
# print(result)
