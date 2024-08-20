from abc import ABC, abstractmethod

class FilePort(ABC):
    @abstractmethod
    def read_file(self, file_content):
        pass

    @abstractmethod
    def write_file(self, content, file_name):
        pass
