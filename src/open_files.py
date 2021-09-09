import pandas as pd
class OpenFiles:
    'this class has opens and closes the file to process using pandas library, it has the openfile method which accepts arguments, accepts either(txt,csv,tsv)'
    def __init__(self,file_type):
        self.file_type  = file_type
    def open_files(self):                                                                                                        
        file_extention = self.file_type.split('.')[-1].lower()  
        pd.set_option('display.max_rows',None,'display.max_columns',None)
        try:
            if file_extention == 'csv':
                yield pd.read_csv(f'./files/{self.file_type}')
            elif file_extention == 'tsv':
                yield pd.read_csv(f'./files/{self.file_type}', sep='\t')
            else: 
                yield pd.read_csv('./files/error_mesages.txt')
        except:
            return 'invalid file format'

class OpenCloseFiles:
    'this class uses the opens files via context manager, accepts either(txt,csv,tsv)'
    def __init__(self,file_type):
        self.file_type  = file_type

    def open_files(self):
                                                                                                                
        file_extention = self.file_type.split('.')[-1].lower() 
        try:
            if file_extention == 'txt' or 'csv' or 'tsv':
                with open(f'./files/{self.file_type}','r') as open_file:return open_file.readlines()
        except:
            with open('./files/error_mesages.txt','r') as read_error:return read_error.readlines()

            