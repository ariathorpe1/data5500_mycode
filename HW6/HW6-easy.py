def sum_of_elements(arr):
   
    if not arr:
        return 0  
    
    return sum(arr)

# Example usage and test cases:
numbers1 = [1, 2, 3, 4, 5]
numbers2 = []
numbers3 = [-1, -2, -3, -4, -5]
numbers4 = [1000000, 2000000, 3000000]

print(sum_of_elements(numbers1))  
print(sum_of_elements(numbers2))  
print(sum_of_elements(numbers3))  
print(sum_of_elements(numbers4))  

'''
Big O Analysis:
The sum() function iterates through all elements once, making the time complexity O(n), where n is the number of elements in the array.
The space complexity is O(1) since we are only using a single variable to store the sum.
'''

