from src.read_bytes_from_file import *
from src.process_spreadsheet import *
import sys



if __name__ ==  '__main__':

    
    read_bytes = ReadBytesFromFile(sys.argv[1])
    # print(read_bytes.read_all()) 
    # print(read_bytes.read_first_two_lines())
    # print(read_bytes.read_last_two_lines())


    
    process_spreadsheet = ProcessSpreadsheet(sys.argv[1])
    # print(process_spreadsheet.read_all())
    # print(process_spreadsheet.read_first_two_lines())
    # print(process_spreadsheet.read_last_two_lines())
     
