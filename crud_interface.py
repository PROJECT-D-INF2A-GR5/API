from abc import ABC, abstractmethod

class CrudABC(ABC):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    @abstractmethod
    def get_conversation():
        pass

    @abstractmethod
    def add_message():
        pass