def MergeArrays2(arr1,arr2):
    mergedArray = arr1 + arr2
    sizeOfArray = len(mergedArray)
    for index1 in range(0, sizeOfArray):
        for index2 in range(index1+1, sizeOfArray):
            if mergedArray[index1] >= mergedArray[index2]:
                mergedArray[index1], mergedArray[index2] = mergedArray[index2],mergedArray[index1]
    return mergedArray

def MergeArrays3(arr1,arr2):
    mergedArray = []
    indexArray1 = 0
    indexArray2 = 0
    while True:
        if arr1[indexArray1]<=arr2[indexArray2]:
            mergedArray.append(arr1[indexArray1])
            indexArray1 += 1
        else:
            mergedArray.append(arr2[indexArray2])
            indexArray2 += 1

        if indexArray1 == (len(arr1)):
            for i in range(indexArray2, len(arr2)):
                mergedArray.append(arr2[i])
            break
        elif indexArray2 == (len(arr2)):
            for j in range(indexArray1,len(arr1)):
                mergedArray.append(arr1[j])  
            break
    return mergedArray

Array1 = [1,3,5]
Array2 = [0,2,5]
print(MergeArrays3(Array1,Array2))
