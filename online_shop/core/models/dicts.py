from django.db import models


class DictProduct(models.Model):
    TYPES = (
        (0, 'Бытовая техника'),
        (1, 'Промышленное оборудование'),
        (2, 'Инструменты'),
        (3, 'Дом, декор и кухня'),
        (4, 'Строительство')
    )
    type = models.IntegerField("Тип", choices=TYPES, primary_key=True)

    def __str__(self):
        return self.get_type_display()
