def fibonacci(n):
    fib = [0,1];
    a,b = 0,1;
    
    for _ in range(2,n):
        c = a+b;
        a = b
        b = c;
        fib.append(c);
    return fib;
print(fibonacci(10))
        

    