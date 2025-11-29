import unittest
import sys
import os

sys.path.append(os.path.dirname(__file__))

from functions import *

def run_all_tests():
    """Run tests"""
    current_dir = os.path.dirname(__file__)
    tests_dir = os.path.join(current_dir, '..', 'tests')
    tests_dir = os.path.abspath(tests_dir) 
    
    loader = unittest.TestLoader()
    suite = loader.discover(tests_dir, pattern='test_*.py')
       
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

def main() -> None:
    run_all_tests()

if __name__ == "__main__":
    main()