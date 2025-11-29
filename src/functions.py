from constants import ERROR_MESSAGES
import heapq

def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using iterative approach.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        n (int): Factorial value of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError(ERROR_MESSAGES['NON_NEGATIVE_NUMBER'])
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        n (int): Factorial value of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError(ERROR_MESSAGES['NON_NEGATIVE_NUMBER'])
    elif n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def fibo(n: int) -> int:
    """
    Calculate the nth Fibonacci number using iterative approach.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        n (int): The nth Fibonacci number
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError(ERROR_MESSAGES['NON_NEGATIVE_NUMBER'])
    
    item = 0
    item_next = 1
    if n == 1:
        return 1
    else:
        for i in range(n - 1):
            item, item_next = item_next, item + item_next
        return item_next

def fibo_recursive(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        n (int): The nth Fibonacci number
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError(ERROR_MESSAGES['NON_NEGATIVE_NUMBER'])
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)

def bubble_sort(a: list, key: callable = None, cmp: callable = None) -> list:
    """
    Sort a list using bubble sort algorithm.
    
    Args:
        a (list): List to be sorted
        key (callable, optional): Function returns a value to use for sorting comparisons.
        cmp (callable, optional): Comparator function that takes two values and returns:
                                 - (-1) if first < second
                                 - 1 if first > second  
                                 - 0 if equal
        
    Returns:
        a (list): Sorted list in ascending order according to the key and comparator
    """
    if len(a) <= 1:
        return a
    
    n = len(a)
    if key is None:
        key = lambda x: x
    
    if cmp is None:
        def cmp(x, y):
            if x < y: return -1
            if x > y: return 1
            return 0
    for i in range(n):
        for j in range(0, n - i - 1):
            left_key = key(a[j])
            right_key = key(a[j + 1])
            
            comparator = cmp(left_key, right_key)
            
            if comparator > 0:
                a[j], a[j + 1] = a[j + 1], a[j]
    
    return a

def quick_sort(a: list[int], key: callable = None, cmp: callable = None) -> list[int]: 
    """
    Sort a list of integers using quick sort algorithm.
    
    Args:
        a (list): List of integers to be sorted
        key (callable, optional): Function returns a value to use for sorting comparisons.
        cmp (callable, optional): Comparator function that takes two values and returns:
                                 - (-1) if first < second
                                 - 1 if first > second  
                                 - 0 if equal
        
    Returns:
        a (list): Sorted list in ascending order according to the key and comparator
    """
    if len(a) <= 1:
        return a
    
    flag_item = a[len(a) // 2]

    r = [x for x in a if x < flag_item]
    l = [x for x in a if x > flag_item]
    c = [x for x in a if x == flag_item]

    if key and cmp:
        flag_item = key(a[len(a) // 2])
        r = [x for x in a if cmp(key(x), flag_item) < 0]
        l = [x for x in a if cmp(key(x), flag_item) > 0]
        c = [x for x in a if cmp(key(x), flag_item) == 0]
    elif key:
        flag_item = key(a[len(a) // 2])
        r = [x for x in a if key(x) < flag_item]
        l = [x for x in a if key(x) > flag_item]
        c = [x for x in a if key(x) == flag_item]
    elif cmp:
        r = [x for x in a if cmp(x, flag_item) < 0]
        l = [x for x in a if cmp(x, flag_item) > 0]
        c = [x for x in a if cmp(x, flag_item) == 0]

    return quick_sort(r, key=key, cmp=cmp) + c + quick_sort(l, key=key, cmp=cmp)

def counting_sort(a: list[int], key: callable = None) -> list[int]:
    """
    Sort a list of integers using counting sort algorithm.
    
    Args:
        a (list): List of integers to be sorted
        key (callable, optional): Function returns a value to use for sorting comparisons.
        
    Returns:
        a (list): Sorted list in ascending order according to the key
    """
    if len(a) <= 1:
        return a
    
    keys = a

    if key:
        keys = [key(x) for x in a]

    max_item = max(keys)
    min_item = min(keys)

    counting_arr = [0] * (max_item - min_item + 1)
    sorted_arr = [0] * len(keys)

    for item in keys:
        index = item - min_item
        counting_arr[index] += 1
    
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]
        
    for i in range(len(a) - 1, -1, -1):
        key_val = keys[i]
        index = counting_arr[key_val - min_item] - 1
        sorted_arr[index] = a[i]
        counting_arr[key_val - min_item] -= 1
    
    return sorted_arr


def radix_sort(a: list[int], key: callable = None, base: int = 10) -> list[int]:
    """
    Sort a list of integers using radix sort algorithm.
    
    Args:
        a (list): List of integers to be sorted
        key (callable, optional): Function returns a value to use for sorting comparisons
        
    Returns:
        a (list): Sorted list in ascending order according to the key
    """

    if len(a) <= 1:
        return a

    keys = a

    if key:
        keys = [key(x) for x in a]
    
    max_key = max(keys)
    max_len = 0
    temp = max_key
    while temp > 0:
        max_len += 1
        temp //= base

    arr = list(zip(keys, a))

    for i in range(max_len):
        bins = [[] for i in range(base)]

        for key_val, item in arr:
            digit = (key_val // (base ** i)) % base
            bins[digit].append((key_val, item))
        
        arr = []

        for k in bins:
            arr.extend(k)
    
    return [item for key_val, item in arr]


def bucket_sort(a: list[float], key: callable = None, cmp: callable = None, buckets: int = 2) -> list[float]: 
    """
    Sort a list of integers using bucket sort algorithm.
    
    Args:
        a (list): List of integers to be sorted
        key (callable, optional): Function returns a value to use for sorting comparisons
        
    Returns:
        a (list): Sorted list in ascending order according to the key
    """
    if len(a) <= 1:
        return a
    
    keys = a

    if key:
        keys = [key(x) for x in a]
    
    if cmp:
        return(quick_sort(a, key=key, cmp=cmp))
    
    max_item = max(keys)
    min_item = min(keys)
    buckets_cnt = buckets
    bucket_size = (max_item - min_item) / buckets_cnt
    r = []

    buckets_list = [[] for i in range(buckets)]

    for ind, val in enumerate(a):
        key_val = keys[ind]
        bucket_index = int((key_val - min_item) / bucket_size)
        if bucket_index >= buckets: 
            bucket_index = buckets - 1
        buckets_list[bucket_index].append(val)

    for bucket in buckets_list:
        if key and cmp:
            sorted_bucket = quick_sort(bucket, key=key, cmp=cmp)
        elif key:
            sorted_bucket = quick_sort(bucket, key=key)
        elif cmp:
            sorted_bucket = quick_sort(bucket, cmp=cmp)
        else:
            sorted_bucket = quick_sort(bucket)
        r.extend(sorted_bucket)
    return r

def heap_sort(a: list[int], key: callable = None) -> list[int]:
    """
    Sort a list of integers using heap sort algorithm.
    
    Args:
        a (list): List of integers to be sorted
        key (callable, optional): Function returns a value to use for sorting comparisons
        
    Returns:
        a (list): Sorted list in ascending order according to the key
    """
    if len(a) <= 1:
        return a
    
    if not key:
        key = lambda x: x
    
    keys = a

    if key:
        keys = [(key(x), x) for x in a]
        heapq.heapify(keys)
        a = [heapq.heappop(keys)[1] for i in range(len(keys))]
    else:
        keys = [(key(x), x) for x in a]
        heapq.heapify(keys)
        a = [heapq.heappop(keys)[1] for i in range(len(keys))]
    
    return a
