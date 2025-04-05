def second_largest(arr):
   
    if len(arr) < 2:
        return None  
    
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else None

# Example usage and test cases:
numbers1 = [10, 20, 4, 45, 99]
numbers2 = [5, 5, 5]
numbers3 = [7]
numbers4 = [1, 2, 3, 4, 5]

print(second_largest(numbers1))  
print(second_largest(numbers2))  
print(second_largest(numbers3))  
print(second_largest(numbers4))  

'''
Big O Analysis:
This solution iterates through the array once, making the time complexity O(n), where n is the number of elements in the array.
The space complexity is O(1) since only two extra variables are used.
'''
