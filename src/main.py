from flask_restful import Api
from resources import HealthCheck as HealthCheckAPI, Product as ProductAPI, ProductList as ProductListAPI
from flask_migrate import Migrate
from app import create_app
from models import db, Product as ProductModel, ProductAttribute as ProductAttributeModel


app = create_app()
migrate = Migrate(app, db)


# API
api = Api(app)
api.add_resource(HealthCheckAPI, '/healthcheck')
api.add_resource(ProductListAPI, '/api/products')
api.add_resource(ProductAPI, '/api/products/<slug>')


# CLI for migrations
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Product=ProductModel, ProductAttribute=ProductAttributeModel)
