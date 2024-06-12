def insertionSort(arr):
    n = len(arr)
      
    # liste muss nicht sortiert werden, falls die liste leer ist oder es nur 1 element gibt
    if n <= 1:
        return  
 
    for i in range(1, n): # Wir fangen beim 2. element (Index 1) an 
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]:  # Werte die Größer sind werden eine position nach rechts verschoben
            arr[j+1] = arr[j]  # Werte werden nach rechts verschoben
            j -= 1
        arr[j+1] = key  # Key wird in der richtigen Position eingefügt 
    


test_list = [73, 52, 66, 41, 12, 18, 4, 19]
print(test_list)
insertionSort(test_list)
print(test_list)