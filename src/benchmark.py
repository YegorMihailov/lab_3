import time
from constants import ERROR_MESSAGES

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
    start = time.perf_counter()
    try:
        func(*args, **kwargs)
    except:
        raise ValueError(ERROR_MESSAGES['EXECUTING_ERROR'])
    end = time.perf_counter()

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
            alg_time = timeit_once(alg(arr))
            res[arr_name][alg_name] = alg_time
    
    return res
