import time
def fib_decorator(func):
    def wrapper():
        starttime=time.perf_counter()
        print("Start : \n",starttime)
        value=func()
        endtime=time.perf_counter()
        print("End : \n",endtime)
        runtime=endtime-starttime
        print("Time Taken = \n",runtime)
        return value
    return wrapper
#@fib_decorator #this line is mandatory
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
dec1=fib_decorator(fib)
dec1()    #these lines are mandatory to show elapsed time

f=fib()
n=int(input("\nEnter value for n\n"))
for i in range(n):
    print(next(f))

    
