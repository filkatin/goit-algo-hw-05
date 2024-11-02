def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return (iterations, arr[mid])
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    # Після завершення циклу, якщо upper_bound не знайдено, встановлюємо його як arr[left]
    if left < len(arr) and (upper_bound is None or arr[left] < upper_bound):
        upper_bound = arr[left]
        
    return (iterations, upper_bound)


#####
sorted_array = [0.5, 1.1, 2.3, 3.7, 4.8, 5.6, 7.2, 9.6, 15.4]
target_value = 6.6

result = binary_search(sorted_array, target_value)
print("Результат:", result)
