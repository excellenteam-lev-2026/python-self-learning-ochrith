from decorator import decorator

@decorator     #twice become a decorator (wrapper function created automatically)
def twice(func, *args, **kwargs):   #*args, **kwargs for each type of function
    func(*args, **kwargs)
    func(*args, **kwargs)



"""#------------------Testing---------------
@twice
def p(s):
    print(s)

p("hello everyone")
"""


