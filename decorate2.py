import time

def performance(unit):
    def per_decorator(f):
        def wrapper(*args, **kw):
            s = time.time()
            r = f(*args, **kw)
            e = time.time()
            if(unit == 's'):
                print 'call %s() %fs' %(f.__name__, e-s)
            if(unit == 'ms'):
                print 'call %s() %fms' %(f.__name__, (e-s)*1000)
            return r
        return wrapper
    return per_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)