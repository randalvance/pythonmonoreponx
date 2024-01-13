from app_domain.entities import Product
from app_domain.repositories import ProductRepository

__all__ = ["ProductRepositoryImpl"]

class ProductRepositoryImpl(ProductRepository):
    def get_all(self):
        return [
            Product(id=1, name='Product 1',description="Product 1",price=10.0)
        ]