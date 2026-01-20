class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
        
import unittest

class Logger(object):  
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

class TestLogger(unittest.TestCase):
    def test_singleton(self):
        logger1 = Logger()
        logger2 = Logger()
        self.assertIs(logger1, logger2)

if __name__ == "__main__":
    unittest.main()
