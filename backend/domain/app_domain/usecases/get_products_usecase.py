from injector import inject

from app_domain.entities import Product
from app_domain.repositories import ProductRepository

__all__ = ["GetProductsUseCase"]

class GetProductsUseCase:
    @inject
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self) -> list[Product]:
        return self.product_repository.get_all()