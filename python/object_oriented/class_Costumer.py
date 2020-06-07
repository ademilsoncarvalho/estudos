class Costumer:
    type = 'admin'

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return 'My name is {}'.format(self.__name.title())

    @name.setter
    def name(self, name):
        self.__name = name

    @staticmethod
    def example_static():
        print('static method')

    @classmethod
    def example_class_method(cls):
        return cls("Ade class method")

    @classmethod
    def example_class_method_attribute(cls):
        return cls.type


if __name__ == '__main__':
    costumer = Costumer('Ademilson')
    costumer.name = "Ade"
    # static method
    costumer.example_static()
    Costumer.example_static()
    # class method
    costumer = Costumer.example_class_method()
    print(Costumer.example_class_method_attribute())
    print(costumer.name)
