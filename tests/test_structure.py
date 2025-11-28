import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.stack import Stack
from src.queue import Queue

class TestStack(unittest.TestCase):  
    def setUp(self):
        """Set up Stack instance before test."""
        self.stack = Stack()
    
    def test_push(self):
        """Test pushing element onto the stack."""
        self.stack.push(1)
        self.assertEqual(len(self.stack), 1, "Stack failed on push")
    
    def test_pop(self):
        """Test popping element from stack."""
        self.stack.push(5)
        self.assertEqual(self.stack.pop(), 5, "Stack failed on pop")
    
    def test_peek(self):
        """Test peeking at the top element without removing it."""
        self.stack.push(42)
        self.assertEqual(self.stack.peek(), 42)
        self.assertEqual(len(self.stack), 1, "Stack failed on peek")
    
    def test_empty_stack(self):
        """ Test operations on an empty stack."""
        self.assertTrue(self.stack.is_empty())
        
        with self.assertRaises(ValueError):
            self.stack.pop()
        
        with self.assertRaises(ValueError):
            self.stack.peek()
    
    def test_min_value(self):
        """Test tracking of minimum value in the stack."""
        self.stack.push(5)
        self.stack.push(2)
        self.stack.push(7)
        self.stack.push(1)
        
        self.assertEqual(self.stack.min, 1)

class TestQueue(unittest.TestCase):
    def setUp(self):
        """Set up Queue instance before test."""
        self.queue = Queue()
    
    def test_enqueue_dequeue(self):
        """
        Test adding element to the queue and removing it."""
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 1)
    
    def test_front(self):
        """Test viewing the front element without removing it."""
        self.queue.enqueue(42)
        self.assertEqual(self.queue.front(), 42)
        self.assertEqual(len(self.queue), 1)
    
    def test_empty_queue(self):
        """Test operations on an empty queue."""
        self.assertTrue(self.queue.is_empty())
        
        with self.assertRaises(ValueError):
            self.queue.dequeue()
        
        with self.assertRaises(ValueError):
            self.queue.front()

if __name__ == '__main__':
    unittest.main()