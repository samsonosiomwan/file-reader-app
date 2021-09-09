from src.file_interface import *
from src.open_files import OpenFiles
            
            
class ProcessSpreadsheet(FileInterface):
    '''this class process a spreadsheet, arguments : file_type (csv,tsv), methods:read_all(reads all file content), read_first_two_lines, read_last_two_lines'''
    def __init__(self,file_type):
        self.file_type = file_type
        #instantiate Openfiles and call open_file method
        self.open_docs = OpenFiles(self.file_type)
        self.read_file = self.open_docs.open_files()

    def read_all(self):
        for lines in self.read_file: return lines

    def read_first_two_lines(self):
        for lines in self.read_file: return lines.head(2)
        
    def read_last_two_lines(self):
        for lines in self.read_file: return lines.tail(2)
        
    


