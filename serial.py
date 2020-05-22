"""Python serial number generator."""

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
    def __init__(self, start=0, current=0):
        """creates an instance of SerialGenerator with attributes: 
        current: int
                 the current value
        start:   int
                 the value to begin the counting at
        """
        self.current = start
        self.start = start

    def __repr__(self):
        return f'<Serial(start={self.start} current={self.current}'

    
    def generate(self):
        """Increments the current and returns the old value"""
        self.current += 1
        return self.current - 1


    def reset(self):
        """starts the count over at the start value"""
        self.current = self.start

    

