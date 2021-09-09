import unittest
from src.process_spreadsheet import *
from src.open_files import *

class Test_ProcessSpreadSheet(unittest.TestCase):
    def setUp(self):
        self.open_file = OpenFiles('text.csv')
        self.read_file = ProcessSpreadsheet('text.csv')
    def test_open_files_csv(self): 
        self.assertIsNotNone(self.open_file.open_files())

    def test_read_all_csv(self):
        self.assertIsNotNone(self.read_file.read_all())
        
        
    def test_read_first_two_lines_csv(self):
        self.assertIsNotNone(self.read_file.read_first_two_lines())
       

    def test_read_last_two_lines_csv(self):
        self.assertIsNotNone(self.read_file.read_last_two_lines())
       

    def tearDown(self):
         self.open_file = None
         self.read_file = None
        

# if __name__ =='__main__':
#     unittest.main()