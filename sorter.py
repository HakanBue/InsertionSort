def insertionSort(arr, firstAtt, secondAtt):
    n = len(arr)
      
    # liste muss nicht sortiert werden, falls die liste leer ist oder es nur 1 element gibt
    if n <= 1:
        return  
 
    for i in range(1, n): # Wir fangen beim 2. element (Index 1) an 
        for i in range(1, len(arr)):
            key = arr[i][firstAtt]
            second_key = arr[i][secondAtt]
            j = i - 1
            while j >= 0 and key > arr[j][firstAtt] or key == arr[j][firstAtt] and second_key > arr[j][secondAtt]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                j -= 1
            arr[j+1][firstAtt] = key


""" test_list = [73, 52, 66, 41, 12, 18, 4, 19]
print(test_list)
insertionSort(test_list)
print(test_list) """