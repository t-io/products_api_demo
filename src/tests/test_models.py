from models import Product, ProductCategories


def test_create_product_slug():
    """Test generating a slug based on product name  """
    name = 'Awesome shirt'
    description = 'The best shirt you can buy for money'
    slug = 'awesome-shirt'
    product = Product(name=name, description=description)

    assert product.name == name
    assert product.description == description
    assert product.slug == slug
    assert product.category == 'uncategorized'  # default fallback


def test_create_product_category():
    """ Test setting category value for string inputs """
    category = 'shirts'

    assert Product.set_category(category) == category
