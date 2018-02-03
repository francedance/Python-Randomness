## To avoid keep using recursive call, we would like to temporary save nth fibonacci number into dictionary
## You can use list(with fixed size) but I would like to use dictionary
cache = {}

def fib_dynamic(n):

    ## Same base cases for n=0 and n=1
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        ## If nth number is not in cache then we would like make one using recursive
        ## So if n = 5, 5th fibonacci number will be inserted to Cache
        if n not in cache:
            cache[n] = fib_dynamic(n-2) + fib_dynamic(n-1)
        ## Return nth fibonacci number if nth is exist inside cache (we know the value, no need to use recursive again!)
        return cache[n]

## Generally speaking, First few inputs will use recursive since cache itself is empty when we start
## As the value of n gets large, for example n=40, if you've inserted n=38, n=39 and Cache has the value for them
## 40th Fibonacci number is simply addition of 38th and 39th which your cache should have! 
## No more Recursive call to find 40th number! So in time wise, this method is faster as value of n gets large!
 
## Testing

for i in range(20):
    print(i+1, 'th Fibonacci number is: ', fib_dynamic(i))