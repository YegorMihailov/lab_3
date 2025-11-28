from .constants import ERROR_MESSAGES

class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, x: int) -> None:
        """
        Add an element to the end of the queue.
        
        Args:
            x (int): The element to be added to the queue
        """
        self.queue.append(x)

    def dequeue(self) -> int:
        """
        Remove and return the front element from the queue.
        
        Returns:
            int: The element removed from the front of the queue
            
        Raises:
            ValueError: If the queue is empty
        """
        if len(self.queue) == 0:
            raise ValueError(ERROR_MESSAGES['EMPTY_LIST'])
        removed = self.queue.pop(0)
        return removed

    def front(self) -> int:
        """
        Return the front element from the queue.
        
        Returns:
            int: The element at the front of the queue
            
        Raises:
            ValueError: If the queue is empty
        """
        if len(self.queue) == 0:
            raise ValueError(ERROR_MESSAGES['EMPTY_LIST'])
        return self.queue[0]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False if queue is not empty
        """
        if len(self.queue) == 0:
            return True
        return False

    def __len__(self) -> int:
        """
        Return the number of elements in the queue.
        
        Returns:
            int: The number of elements in the queue
        """
        return len(self.queue)
