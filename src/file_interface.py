from abc import ABC, abstractmethod
class FileInterface(ABC):
    '''this class is an abstract class which stands as the interface for ReadFiles Class. it contains read_all(),read_first_two_lines(), read_last_two_lines() methods''' 
    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_first_two_lines(self):
        pass
    
    @abstractmethod
    def read_last_two_lines(self):
        pass