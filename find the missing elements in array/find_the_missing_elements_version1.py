def finder(arr1,arr2):
    
    dict = {}
    
    for i in arr1:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
        
    for j in arr2:
        if j in dict:
            dict[j] -= 1
    
    for k in dict:
        if dict[k] != 0:
            print(k, 'is the missing number in Second Array!')

   

    
   # print(missing)

# Testing
arr1 = [1,2,3,4,5,6,7]
arr2 = [8,9,10,11]
finder(arr1,arr2)