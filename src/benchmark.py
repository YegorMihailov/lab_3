import time
from constants import ERROR_MESSAGES
from functions import quick_sort, bubble_sort

def timeit_once(func, *args, **kwargs) -> float:
    """
    Measure the execution time of a function call.
    
    Args:
        func (callable): The function to time
        *args: Positional arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function
        
    Returns:
        float: Execution time in seconds
        
    Raises:
        ValueError: If the function execution fails
    """
    start = time.time()
    try:
        func(*args, **kwargs)
    except:
        raise ValueError(ERROR_MESSAGES['EXECUTING_ERROR'])
    end = time.time()

    return end - start

def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    """
    Benchmark multiple sorting algorithms on multiple arrays.
    
    Args:
        arrays (dict[str, list]): Dictionary of arrays and their names
        algos (dict[str, callable]): Dictionary of sorting functions and their names
        
    Returns:
        dict[str, dict[str, float]]: Dictionary with timing results.
                                     Structure: {array_name: {algorithm_name: time}}
    """
    res = {}
    for arr_name, arr in arrays.items():
        res[arr_name] = {}
        for alg_name, alg in algos.items():
            test_arr = arr.copy()
            start = time.perf_counter()
            alg(test_arr)
            end = time.perf_counter()

            alg_time = end - start
            res[arr_name][alg_name] = alg_time
    
    return res

arrs = {
    'bebra': [1, 345, 3452, 3, 32, 2, -54],
    'huyamba': [34, 443, 34, 232, 232, 324234, 324]
}

algos = {
    'quick': quick_sort,
    'bubble': bubble_sort
}

# print(benchmark_sorts(arrs, algos))
