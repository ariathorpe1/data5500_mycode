def max_difference(arr):
   
    if len(arr) < 2:
        return None  
    
    min_num = min(arr)
    max_num = max(arr)
    return max_num - min_num

# Example usage and test cases:
numbers1 = [1, 2, 90, 10, 110]
numbers2 = [5, 5, 5, 5]
numbers3 = [-10, -20, -30, -5]
numbers4 = [100, 200, 300, 400, 500]

print(max_difference(numbers1))  
print(max_difference(numbers2))  
print(max_difference(numbers3))  
print(max_difference(numbers4))  

'''
Big O Analysis:
Finding the min and max values each take O(n), so the total time complexity is O(n).
The space complexity is O(1) since we only store two variables for min and max.
'''

