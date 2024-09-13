# runtime_measure.py

import time
from contextlib import contextmanager

@contextmanager
def measure_runtime():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"Runtime: {end_time - start_time:.4f} seconds")

def measure_function_runtime(func,iter=1, *args, **kwargs):
    start_time = time.time()
    result = -1
    for i in range(iter):    
        result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Runtime of {func.__name__} for {iter} iterations: {(end_time - start_time)/iter:.4f} seconds")
    return result
