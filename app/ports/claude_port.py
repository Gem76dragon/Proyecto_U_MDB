from abc import ABC, abstractmethod

class ClaudePort(ABC):
    @abstractmethod
    def generate_response(self, prompt, temperature, max_tokens):
        pass
