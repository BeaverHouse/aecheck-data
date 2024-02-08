from functools import wraps
import time

# From https://dev.to/kcdchennai/python-decorator-to-measure-execution-time-54hk
def time_check(func):
    @wraps(func)
    def time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return time_wrapper