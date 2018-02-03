
## Recursive string reversal! note: no iteration! no slicing(I meant [::-1] method! just recursive!
## Defining reverse function
## Where 's' == string argument
def reverse(s):

    ## Base case in which if length of string is 1, or less just return itself
    if len(s) <= 1:
        return s
    
    ## Recursive approach to reverse
    else:
        ## s[len(s)-1] is basically the last character of any given string argument
        ## '+' operation is simply concatenation of two string values
        ## reverse(s[:len(s)-1]) is basically a recursive call
        ## Note that everytime when we call recursive, we're passing sliced string from beginning to last character 
        ## len(s)-1 gives you the index number of last character of current 's' value
        ## s[:len(s)-1] gives you all the other characters before last character of current 's' value
        ## For a breakdown:
        ## s = 'Hello World', after first stage of function:
        ## 'd' + reverse('Hello Worl') becomes <- note! we're passing 'Hello Worl' without 'd'
        ## 'd' + 'l' + reverse('Hello Wor') becomes
        ## 'd' + 'l' + 'r' + reverse('Hello Wo') ... until s's length become '1':base case

        return s[len(s)-1] + reverse(s[:len(s)-1])
        

## Testing

print('Hello Word reversed: ', reverse('Hello World')) 
print('123456789 reversed: ', reverse('123456789')) 
print('abcdefghijk reversed: ', reverse('abcdefghijk'))
print('aa reversed:', reverse('aa'))
