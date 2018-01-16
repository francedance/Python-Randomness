def pair_sum(arr,k):

    # Edge checking
    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:

        # For exmaple, given that you have arr = [1,3,2,2] and k = 4
        # target = k - num, target = (4) - (1) = (3) on first loop. 
        # It is like finding: (1) + (target) = 4, since we're finding sets that sums upto 4. 

        target = k - num

        if target not in seen:
            seen.add(num)
        
        else:
            output.add(((min(num,target)), max(num,target)))
        
    print('\n'.join(map(str,list(output))))

# Testing

pair_sum([1,3,2,2],4)

# should output:
# (1,3)
# (2,2)