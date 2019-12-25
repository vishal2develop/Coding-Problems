
#Given an array with repeated elements, find the maximum distance between two occurrences of all the elements in the array.

def maxDistance(arr): 
    n=len(arr)
    # Used to store element to first index mapping 
    mp = {} 
    # Traverse elements and find maximum distance between 
    # same occurrences with the help of map. 
    maxDict = 0
    for i in range(n): 
        # If this is first occurrence of element, insert its 
        # index in map 
        if arr[i] not in mp.keys(): 
            mp[arr[i]] = i 
        # Else update max distance 
        else: 
            maxDict = max(maxDict, i-mp[arr[i]]) 
    return maxDict 

#driver code
arr = list(map(int,"3,2,1,2,1,4,5,8,6,7,4,2".split(',')))
print(maxDistance(arr)) 
