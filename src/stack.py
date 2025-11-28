from .constants import ERROR_MESSAGES

class Stack:
    def __init__(self):
        """Initialize empty stack."""
        self.stack = []
        self.min_val = None

    def push(self, x: int) -> None:
        """
        Push an element onto the stack.
        
        Args:
            x (int): The element to be pushed onto the stack
        """
        self.stack.append(x)
        if len(self.stack) == 1 or x < self.min:
            self.min = x

    def pop(self) -> int:
        """
        Remove and return the top element from the stack.
        
        Returns:
            int: The element removed from the top of the stack
            
        Raises:
            ValueError: If the stack is empty
        """
        if len(self.stack) == 0:
            raise ValueError(ERROR_MESSAGES['EMPTY_LIST'])
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
        elif removed == self.min:
            self.min = self.stack[0]
            for i in self.stack:
                if i < self.min:
                    self.min = i
        return removed

    def peek(self) -> int:
        """
        Return the top element from the stack without removing it.
        
        Returns:
            int: The element at the top of the stack
            
        Raises:
            ValueError: If the stack is empty
        """
        if len(self.stack) == 0:
            raise ValueError('EMPTY_LIST')
        return self.stack[-1]

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False if stack is not empty
        """
        if len(self.stack) == 0:
            return True
        return False

    def __len__(self) -> int:
        """
        Return the number of elements in the stack.
        
        Returns:
            int: The number of elements in the stack
        """
        return len(self.stack)

    def min(self) -> int:
        """
        Return the minimum element in the stack.
        
        Returns:
            int: The minimum element in the stack
        """
        return self.min_val