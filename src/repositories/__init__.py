from flask_sqlalchemy import SQLAlchemy
from .products import ProductRepository


db = SQLAlchemy()
__all__ = ['ProductRepository']
