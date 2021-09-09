import unittest
from src.read_bytes_from_file import *
from src.open_files import *

class Test_ReadBytesFromFile(unittest.TestCase):
    def setUp(self):
        self.open_file = OpenCloseFiles('text.txt')
        self.read_file = ReadBytesFromFile('text.txt')
        
    def test_open_files(self):
        self.assertIsNotNone(self.open_file.open_files())
        self.assertIsInstance(self.open_file.open_files(),list)
    
    def test_read_all(self):
        self.assertIsNotNone(self.read_file.read_all())
        self.assertIsInstance(self.read_file.read_all(),str)

    def test_read_first_two_lines(self):
        self.assertIsNotNone(self.read_file.read_first_two_lines())
        self.assertIsInstance(self.read_file.read_first_two_lines(),str)
    def test_read_last_two_lines(self):
        self.assertIsNotNone(self.read_file.read_last_two_lines())
        self.assertIsInstance(self.read_file.read_last_two_lines(),str)

    def tearDown(self):
         self.read_file = None
         self.open_file = None
        

# if __name__ =='__main__':
#     unittest.main()