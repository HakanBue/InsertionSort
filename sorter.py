from Bug import Bug, read_csv_to_bugs

def insertion_sort(arr, *sort_by):
    n = len(arr)
      
    if n <= 1:
        return arr

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and compare(arr[j], key, sort_by) > 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def compare(bug1, bug2, sort_by):
    for attr in sort_by:
        value1 = getattr(bug1, attr)
        value2 = getattr(bug2, attr)
        if value1 < value2:
            return -1
        elif value1 > value2:
            return 1
    return 0

# Example usage
csv_file_path = 'Bugreport_fixed_csv.csv'
bugs_list = read_csv_to_bugs(csv_file_path)

# Sorting bugs by severity, priority, and creation_date using insertion sort
sorted_bugs = insertion_sort(bugs_list, 'severity')

# Check the first entries after sorting
for bug in sorted_bugs:
    print(f'{vars(bug)} \n')