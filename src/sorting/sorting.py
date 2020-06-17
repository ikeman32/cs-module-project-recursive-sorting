# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrL, arrR):
    #created the merged array of zeros with the
    #length times the sum of the lengths of arrA and arrB
    merged_arr = [0] * (len(arrL) + len(arrR))

    #Left and Right index
    l_idx, r_idx = 0, 0

    #for loop staring w/index of 0 and ending w/len of merged_arr
    for i in range(0, len(merged_arr)):
        #start with left
        if l_idx >= len(arrL):#if l_idx greater or equal to len of arrL
            merged_arr[i] = arrR[r_idx]#merge arrR[current idx]
            r_idx += 1#increase idx
        #goto right
        elif r_idx >= len(arrR):#if r_idx greater or equal to len of arrR
            merged_arr[i] = arrL[l_idx]#merge arrL[current idx]
            l_idx += 1#increase idx
        #compare left and right
        elif arrR[r_idx] < arrL[l_idx]:#if r less than l
            merged_arr[i] = arrR[r_idx]#merge arrR
            r_idx += 1#increase idx
        #otherwise
        else:
            merged_arr[i] = arrL[l_idx]#merge arrL
            l_idx += 1#increase idx

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    #base case
    if len(arr) <= 1:
        return arr
    

    #recursive function call to divide every element between l and r
    
    l,r = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])

    arr = merge(l, r)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

