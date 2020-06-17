# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, low, high):
    #Check base case
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == target: #Base case
            return mid

        elif arr[mid] > target: #call to self and move toward base
            return binary_search(arr, target, low, mid - 1)

        else:
            return binary_search(arr, target, mid + 1, high)
    else:
        return -1 # not found

'''
From the test file
f=Function call a=arr t=target l=low h=high 
self.assertEqual(binary_search(arr1, -8, 0, len(arr1)-1), 1)
                    f^         a^    t^ l^  h^--------^   ^what is this?
'''

'''def binary_search(arr, target):
    #Set high and low
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        #Set mid range
        mid = low + high // 2

        #If less than target ignore everything on the left
        if arr[mid] < target:
            low = mid + 1
        #if greater than target ignore everythin on the right
        elif arr[mid] > target:
            high = mid - 1
        #Otherwise return the result
        else:
            return mid

    return -1  # not found'''

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

