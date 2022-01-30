cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    
    
        
    # return a list of fibonacci numbers
    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    return fib[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))