from functools import wraps

#create a custom exception
class myTypeException (Exception):  
    def __init__(self, expected, received):
        message=f"Invalid type of parameter. Expected {expected}, and {received} received !"
        super().__init__(message)

def type_check(param_type):
    def decorator(func):

        @wraps(func)  #to keep the information of func
        def wrapper(x):
            if not isinstance(x,param_type):
                raise myTypeException(param_type,type(x))

            else:
                return func(x)

        return wrapper


    return decorator

#---------------Testing-------------------

decorator=type_check(float)
@decorator #will call decorator(function) and function will call wrapper(x)
def function(x):
    print(x)
    return x


function(0.2)
