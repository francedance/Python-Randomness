## For example, if you pass '12345' the function returns all the sum of single digit 
## in this case, the function will return 1+2+3+4+5 = 15

def sum_func(n):
    ## Base case when number is single digit by itself, when a number only contains 1 digit.
    if len(str(n)) == 1:
        return n
    else:
        ## n % 10 returns the last digit, for example, 12345 % 10 = 5 (last digit)
        ## n // 10 (Python 3), n / 10 (Python 2). trims the last digit leaving remaining number
        ## 12345 // 10 = 1234 (We want to pass this number into function to perform recursion)
        ## Overall
        ## 12345 is passed , 5 + sum_func(1234) => 5 + 4 + sum_fun(123) => 5 + 4 + 3 + sum_fun(12) + .. + 1
          
        return (n % 10 ) + sum_func (n // 10)

## Testing

print(sum_func(12345)) ## should return 15!
