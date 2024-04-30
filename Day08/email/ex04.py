

import time

def elapsed(func):
    def wrapper():
        start =time.time()
        result = func()
        end = time.time()
        print('함수 수행 시간 : {} 초'.format(end - start))
        return result
    return wrapper

@elapsed
def my_func():
    time.sleep(3)
    print('함수 수행')

answer = my_func()