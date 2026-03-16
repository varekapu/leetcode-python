def fibonacciNonRecursive(n) -> list:
    try:
        fib = [0, 1]
        for i in range(2, n + 1):
            newFib = fib[i - 1] + fib[i - 2]
            fib.append(newFib)
        print(fib)  
    except ValueError:
        print("please enter valid values")    

print("Fibonacci series output:")
#fibonacciNonRecursive(10)
#negative test case 
fibonacciNonRecursive(3)
