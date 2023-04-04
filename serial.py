"""Python serial number generator."""
from itertools import count
class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start =0):
        """Make a new generator, starting at start."""
        self.start = self.next = start

    def __rer__(self):
        return "f(SerialGenerator start={self.a} next={self.next})"
    
    def generate(self):
        """Return next serial"""

        self.next +=1
        return self.next
    
    def reset(self):
        """Reset number to original start"""


        
        