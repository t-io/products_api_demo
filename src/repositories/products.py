from sqlalchemy.exc import IntegrityError
from exceptions import ResourceExists, InvalidInputData
from models import Product, ProductCategories


class ProductRepository:

    @staticmethod
    def validate_category(category: str) -> bool:
        if any(x for x in ProductCategories if x.value == category):
            return True
        return False

    def validate(self, raw_data: dict) -> bool:
        validation = []
        if 'category' in raw_data:
            validation.append(self.validate_category(raw_data['category']))
        return all(validation)

    def create(self, name: str, description: str, category: str = ProductCategories.uncategorized.value) -> dict:
        if not self.validate({'name': name, 'description': description, 'category': category}):
            raise InvalidInputData()

        try:
            product = Product(name=name, description=description, category=category)
            product.save()
            return {
                'slug': product.slug,
                'name': product.name,
                'description': product.description,
                'category': ProductCategories(product.category).name,
                'created_at': str(product.created_at),
                'updated_at': str(product.updated_at),
            }
        except IntegrityError:
            Product.rollback()
            raise ResourceExists('Product already exists')

    @staticmethod
    def get(product_slug: str) -> dict:
        product = Product.query.filter_by(slug=product_slug).first_or_404()
        return {
            'slug': product.slug,
            'name': product.name,
            'description': product.description,
            'category': product.category.value,
            'created_at': str(product.created_at),
            'updated_at': str(product.updated_at),
        }
