import time

#test with  time.time() and  time.perf_counter
def timer(f,*args,**args2):
    start1=time.time()
    start2=time.perf_counter()
    f(*args,**args2)
    end1=time.time()
    end2=time.perf_counter()
    print("Duration of " ,f.__name__," function with time.time(): ",end1-start1)
    print(" Duration of " ,f.__name__," function with perf_counter:  ",end2-start2)



timer("Hi {name}".format, name="Bug")
timer(zip,[1,2,3],[4])
