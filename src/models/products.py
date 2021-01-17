from datetime import datetime
from enum import Enum
from flask_sqlalchemy import SQLAlchemy
from slugify import slugify
from .abc import BaseModel


db = SQLAlchemy()


class ProductCategories(Enum):
    uncategorized = 'uncategorized'
    shoes = 'shoes'
    shirts = 'shirts'
    jackets = 'jackets'


class Product(db.Model, BaseModel):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    category = db.Column(db.Enum(ProductCategories), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    set_delete = db.Column(db.Boolean, default=False)

    @staticmethod
    def set_category(category_name: str):
        category_value = 'uncategorized'
        if category_name in [c.value for c in ProductCategories]:
            return category_name
        return category_value

    def __init__(self, name: str, category: str = '', description: str = '', set_delete: bool = False):
        self.name = name
        self.slug = slugify(name)
        self.category = self.set_category(category)
        self.description = description
        self.set_delete = set_delete


db.Index('productCategory', Product.category)


class ProductAttribute(db.Model, BaseModel):
    __tablename__ = 'product_attributes'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    name = db.Column(db.String(255), nullable=False)
    data = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, product_id: int, name: str, data: dict):
        self.product_id = product_id
        self.name = name
        self.data = data
