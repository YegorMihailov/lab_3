import random
from .constants import ERROR_MESSAGES
# docstring
# нужно использовать тест кейсы в тестах

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Generate random array of integers.
    
    Args:
        n (int): Number of elements in the array
        lo (int): Lower bound for random values (inclusive)
        hi (int): Upper bound for random values (inclusive)
        distinct (bool, optional): If True, all values will be distinct. Defaults to False
        seed (optional): Random seed for reproducible results
        
    Returns:
        list[int]: Random array of integers
        
    Raises:
        ValueError: If distinct is True and not enough distinct values in range
    """
    if seed:
        random.seed(seed)
    
    if distinct:
        if hi == lo:
            raise ValueError(ERROR_MESSAGES['NOT_ENOUGH_DISTINCT_VALUES'])
        return random.sample(range(lo, hi + 1), n)
    
    return [random.randint(lo, hi) for i in range(n)]

def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Generate a nearly sorted array.
    
    Args:
        n (int): Number of elements in the array
        swaps (int): Number of random swaps
        seed (optional): Random seed for reproducible results
        
    Returns:
        list[int]: Nearly sorted array of integers
    """
    if seed:
        random.seed(seed)

    arr = [x for x in range(n)]

    for k in range(swaps):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Generate an array with many duplicate values.
    
    Args:
        n (int): Number of elements in the array
        k_unique (int, optional): Number of unique values.
        seed (optional): Random seed for reproducible results
        
    Returns:
        list[int]: Array with many duplicate values
    """
    if seed:
        random.seed(seed)
    
    unique = [random.randint(1, 100) for i in range(k_unique)]

    return [random.choice(unique) for i in range(n)]

def reverse_sorted(n: int) -> list[int]:
    """
    Generate a reverse sorted array in descending order.
    
    Args:
        n (int): Number of elements in the array
        
    Returns:
        list[int]: Reverse sorted array from n down to 0
    """
    
    return [x for x in range(n, 0, -1)]

def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Generate a random array of floating-point numbers.
    
    Args:
        n (int): Number of elements in the array
        lo (float, optional): Lower bound for random values
        hi (float, optional): Upper bound for random values
        seed (optional): Random seed for reproducible results
        
    Returns:
        list[float]: Random array of floating-point numbers
    """
    if seed:
        random.seed(seed)
    
    return [random.uniform(lo, hi) for i in range(n)]

# print(rand_float_array(3, 1.5, 4.5))

