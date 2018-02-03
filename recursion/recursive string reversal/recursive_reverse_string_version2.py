def reverse(s):

    if len(s) <= 1:
        return s
    else:
        ## The trick here is putting first element at the end of concatenation
        ## Then slicing string from 1st character to rest (since we've popped out first character)
        ## Breakdown:
        ## s = 'Reverse', on first stage:
        ## reverse('everse') + 'R', second stage:
        ## reverse('verse') + 'e' + 'R' , thrid stage:
        ## reverse('erse') + 'v' + 'e' + 'R' , fourth stage:
        ## reverse('rse') + 'e' + 'v' + 'e' + 'R' , at the end:
        ## 'e' + 's' + 'r' + 'e' + 'v' + 'e' + 'R' = 'esreveR'!
        
        return reverse(s[1:]) + s[0]



## Testing

print('Hello Word reversed: ', reverse('Hello World')) 
print('123456789 reversed: ', reverse('123456789')) 
print('abcdefghijk reversed: ', reverse('abcdefghijk'))
print('aa reversed:', reverse('aa'))
