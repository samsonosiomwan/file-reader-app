import itertools
from abc import ABC,abstractmethod
from src.file_interface import *
from src.open_files import OpenCloseFiles


class ReadBytesFromFile(FileInterface):
    '''this class process a spreadsheet, arguments : file_type (csv,tsv), methods:read_all(reads all file content), read_first_two_lines, read_last_two_lines'''

    def __init__(self,file_type):
        
        self.file_type = file_type
        #instantiate OpenCloseFiles class and call open file method
        self.open_docs = OpenCloseFiles(self.file_type)
        self.read = self.open_docs.open_files()
        self.file_content_length = len(self.open_docs.open_files())

    def read_all(self):
        lines = list(itertools.islice(self.read,self.file_content_length))
        return ''.join(lines)
              
    
    def read_first_two_lines(self):
        lines = list(itertools.islice(self.read,2))
        return ''.join(lines)
    
    def read_last_two_lines(self):
        lines = list(itertools.islice(self.read,self.file_content_length-2,self.file_content_length))
        return ''.join(lines)






