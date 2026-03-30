


def surprise(func):
    def wrapper(*args, **kwargs):   #i had (*args, **kwargs)  in the wrapper arg because i want it work for each type of function !
        print("surprise")    #no call of func !
    return wrapper


#--------Testing---------
@surprise    #the decorator will call surprise(f) -->wrapper(x)
def f(x):
    return x**2
f("qhb",55,p=5)
