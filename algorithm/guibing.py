#归并排序，采用分而治之的思想，不断的将列表拆分为一半，排序完成后，执行合并的操作
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefhalf = arr[:mid]
        righthalf = arr[mid:] 

        mergeSort(lefhalf) #左排序
        mergeSort(righthalf) #右排序

        #将两个有序合并
        i = 0 #left length
        j = 0 #right length
        k = 0 #新数组的下标

        while i < len(lefhalf) and j < len(righthalf):
            if lefhalf[i] < righthalf[j]:
                arr[k] = lefhalf[i]
                i = i+1
            else:
                arr[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefhalf):
            arr[k] = lefhalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j+1
            k = k+1        


arr = [54,26,93,17,77,31,44,55,20]
mergeSort(arr)
print(arr)