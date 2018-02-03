def fib_recursive(n):

    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fib_recursive(n-2) + fib_recursive(n-1)

## Testing

## 10th number in Fibonnaci Sequence
print(fib_recursive(10))
## 0th number in Fibonnaci Sequence
print(fib_recursive(0))
## 1th number in Fibonnaci Sequence
print(fib_recursive(1))
## 16th number in Fibonnaci Sequence
print(fib_recursive(16))

list = []
print('Fibonnaci Sequence of First 30 numbers: ')
for i in range(30): 
    list.append(fib_recursive(i))

print(list)