from abc import ABC, abstractmethod

from app_domain.entities import Product

__all__ = ["ProductRepository"]

class ProductRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Product]:
        pass
