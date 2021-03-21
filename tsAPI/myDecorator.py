import time

def countTime(func):
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        print('cost time:', time.time() - start)
    return wrapper
