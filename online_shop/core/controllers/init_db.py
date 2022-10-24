from core.models.dicts import DictProduct


class InitorCore:
    def init(self):
        self.init_abstract_dict(DictProduct)

    def init_abstract_dict(self, model):
        for t in model.TYPES:
            model.objects.get_or_create(type=t[0])
        print("Инициализация типов продуктов завершена")