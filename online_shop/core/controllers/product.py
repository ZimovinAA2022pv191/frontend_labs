from core.models import Product


class ProductController:
    def __init__(self, pk: int = None):
        self.product = None
        if pk:
            self.product = Product.objects.get(id=pk)

    def create(self, name, price, description, type_product):
        self.product = Product(
            name=name,
            price=price,
            description=description,
            type_product=type_product
        )
        self.product.save()
        return self.product

    @staticmethod
    def delete(product: Product):
        product.delete()
