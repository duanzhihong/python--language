def bubblingSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr
alist = [54,26,93,17,77,31,44,55,20]
arr = bubblingSort(alist)
print(arr)


