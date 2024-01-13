from injector import Injector
from fastapi import FastAPI
from fastapi_injector import attach_injector, Injected

from app_domain.repositories import ProductRepository
from app_domain.usecases import GetProductsUseCase
from app_platform.repositories import ProductRepositoryImpl

app = FastAPI()

injector = Injector()
injector.binder.bind(ProductRepository, ProductRepositoryImpl())
attach_injector(app, injector)

@app.get("/")
def get_home(usecase: GetProductsUseCase = Injected(GetProductsUseCase)):
    return usecase.execute()