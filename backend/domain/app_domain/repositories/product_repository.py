from abc import ABC, abstractclassmethod

class ProductRepository(ABC):
    @abstractclassmethod
    def get_all(self):
        pass
