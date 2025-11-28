import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.functions import *
from src.test_cases import *

class TestSorting(unittest.TestCase):
    
    def setUp(self):
        """Initialize test data for sorting algorithms"""
        
        self.test_arrays = {
            'small_random': [3, 1, 4, 1, 5, 9, 2, 6],
            'sorted': [1, 2, 3, 4, 5],
            'single_element': [42],
        }
    
    def test_bubble_sort(self):
        """Test bubble sort algorithm with various input arrays"""

        for name, arr in self.test_arrays.items():
            with self.subTest(array=name):
                expected = sorted(arr)
                result = bubble_sort(arr)
                self.assertEqual(result, expected, f"Bubble sort failed on {name}")
    
    def test_quick_sort(self):
        """Test quick sort algorithm with various input arrays"""
        for name, arr in self.test_arrays.items():
            with self.subTest(array=name):
                expected = sorted(arr)
                result = quick_sort(arr)
                self.assertEqual(result, expected, f"Quick sort failed on {name}")
    
    def test_counting_sort(self):
        """Test counting sort algorithm with various input arrays"""

        test_data = {
            'default_arr': [3, 1, 4, 1, 2],
            'single': [5],
            'empty': [],
        }
        
        for name, arr in test_data.items():
            with self.subTest(array=name):
                expected = sorted(arr)
                result = counting_sort(arr)
                self.assertEqual(result, expected, f"Counting sort failed on {name}")
    
    def test_radix_sort(self):
        """"Test radix sort algorithm with various input arrays"""

        for name, arr in self.test_arrays.items():
            with self.subTest(array=name):
                expected = sorted(arr)
                result = radix_sort(arr)
                self.assertEqual(result, expected, f"Radix sort failed on {name}")
    
    def test_heap_sort(self):
        """Test heap sort algorithm with various input arrays"""
        for name, arr in self.test_arrays.items():
            with self.subTest(array=name):
                expected = sorted(arr)
                result = heap_sort(arr)
                self.assertEqual(result, expected, f"Heap sort failed on {name}")
    
    def test_bucket_sort(self):
        """Test bucket sort algorithm with various input arrays"""       
        for name, arr in self.test_arrays.items():
            with self.subTest(array=name):
                expected = sorted(arr)
                result = bucket_sort(arr, buckets=5)
                self.assertEqual(result, expected, f"Bucket sort failed on {name}")
    
    def test_sort_key(self):
        """Test sorting algorithms with key function"""

        arr = ["apple", "hi", "banana", "a"]
        expected = sorted(arr, key=len)
        
        result_bubble = bubble_sort(arr, key=len)
        result_quick = quick_sort(arr, key=len)
        result_heap = heap_sort(arr, key=len)
        result_counting = counting_sort(arr, key=len)
        result_radix = radix_sort(arr, key=len)
        result_bucket = bucket_sort(arr, key=len)
        
        self.assertEqual(result_bubble, expected, "Bubble sort failed with key")
        self.assertEqual(result_quick, expected, "Quick sort failed with key")
        self.assertEqual(result_heap, expected, "Heap sort failed with key")
        self.assertEqual(result_counting, expected, "Counting sort failed with key")
        self.assertEqual(result_radix, expected, "Radix sort failed with key")
        self.assertEqual(result_bucket, expected, "Bucket sort failed with key")
    
    def test_sort_comparator(self):
        """Test sorting algorithms with comparator function"""
        def reverse_cmp(a, b):
            if a < b: return 1
            if a > b: return -1
            return 0
        
        arr = [3, 1, 4, 1, 5]
        expected = sorted(arr, reverse=True)
        
        result_bubble = bubble_sort(arr, cmp=reverse_cmp)
        result_quick = quick_sort(arr, cmp=reverse_cmp)
        result_bucket = bucket_sort(arr, cmp=reverse_cmp)
        
        self.assertEqual(result_bubble, expected, "Bubble sort failed with comparator")
        self.assertEqual(result_quick, expected, "Quick sort failed with comparator")
        self.assertEqual(result_bucket, expected, "Bucket sort failed with comparator")

if __name__ == '__main__':
    unittest.main()