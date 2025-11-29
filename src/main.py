import unittest
import os

from functions import *

def run_all_tests():
    """Run tests"""
    current_dir = os.path.dirname(__file__)
    tests_dir = os.path.join(current_dir, '..', 'tests')
    
    loader = unittest.TestLoader()
    suite = loader.discover(tests_dir, pattern='test_*.py')
       
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

def main() -> None:
    run_all_tests()

if __name__ == "__main__":
    main()