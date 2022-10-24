from core.models import Image


class ImagesController:

    def get_images(self, product_id=None):
        images = Image.objects.filter()
        if product_id:
            images = images.filter(product__id=product_id)
        return images
