n = 4
a = 0
b = 1

ans = 0

def fib(n,a,b):
    for i in range(n-1):
        ans = a + b
        a = b
        b = ans
        #print(ans)
    return ans


print(fib(n,a,b))


    

    

