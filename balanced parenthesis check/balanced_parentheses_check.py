## This code only works assuming there is no characters between parenthesis

def balance_check(s):

    ## Just an edge checking!
    if len(s)%2 != 0:
        return False

    ## Defining opening parenthesis
    opening = set('([{') 

    ## Defining a set of matching parenthesis
    matches = set([ ('(',')') , ('[',']') , ('{','}') ])
    
    ## Defining an empty stack
    stack = []

    ## Looping through String that was passed 
    for parenthesis in s:

        ## If current position of String is one of opening, append it to stack
        if parenthesis in opening:
            stack.append(parenthesis)
        
        ## If current position of String isn't opening: meaning it could be closing, character and etc.
        else:
            ## If stack is empty, it means there is no balanced parenthesis so return False
            if len(stack) == 0:
                return False

            ## At this point, there has to be at least one opening parenthesis inside Stack. 
            ## Popping stack will let us know what's the last opening parenthesis is
            last_open = stack.pop()

            # We know current parenthesis is closing but no clue whether it is ] , } , or ). 
            # We can simply borrow our knowledge of last opening parenthesis.
            # If current parenthesis and last open parenthesis matches to one of our matches set. It is balanced
            
            if (last_open,parenthesis) not in matches:
                return False
    
    return len(stack) == 0

## Testing
print(balance_check('[]'))
print(balance_check('[({})]'))
print(balance_check('[{]}]'))
print(balance_check('[{}]'))