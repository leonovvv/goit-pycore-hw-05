def caching_fibonacci():
    #Cache dictionary
    cache = {}

    def fibonacci(n):
        #Default cases
        if n == 0: return 0
        if n == 1: return 1

        #If Nth Fibonacci number is cached - return it from cache
        if n in cache:
            return cache[n]

        #Calculate and cache Nth number with (n-2) as first argument to shorten call stack
        #With (n-1) first and recursion limit 1000 i was able to calculate max N=986
        #With (n-2) first and recursion limit 1000 i was able to calculate max N=1970
        cache[n] = fibonacci(n - 2) + fibonacci(n - 1)

        return cache[n]
    
    return fibonacci

# Get fibonacci function with cache
fib = caching_fibonacci()

#Some examples
print(fib(10))
print(fib(15))
