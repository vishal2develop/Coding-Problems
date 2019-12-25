def smallMissingNumber(a, n) :  
      
    #unordered map 
    mp = dict();  
  
    #checking value of array is positive or not
    #if positive, store in mp 
    for i in range(n) : 
        if (a[i] > 0) : 
            if a[i] not in mp.keys() : 
                mp[a[i]] = 0
            
            mp[a[i]] += 1
  
    index = 1;  # As 1 is the smallest positive integer
    #print(mp)
 
    while (1) : 
        if (index not in mp.keys()) :  # checking if 1 is present in mp
            return index;  
          
  
        index += 1;  

  
arr = [ -5, 2,1, 0, -1, -10, 15 ];  
size = len(arr);  
  
print("Smallest positive missing number is : ",smallMissingNumber(arr, size));  
