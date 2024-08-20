from abc import ABC, abstractmethod

class UIPort(ABC):
    @abstractmethod
    def display_text(self, text, header=None):
        pass

    @abstractmethod
    def get_user_input(self, input_type, label, **kwargs):
        pass
