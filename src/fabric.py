from abc import ABC, abstractmethod


class Product(ABC):
    pass


class FirstProduct(Product):
    pass


class SecondProduct(Product):
    pass


class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass

    def print_product_class(self):
        product = self.create_product()
        return product.__class__


class FirstFactory(Factory):
    def create_product(self):
        return FirstProduct()


class SecondFactory(Factory):
    def create_product(self):
        return SecondProduct()



def func(factory: Factory) -> None:
    print(f"Product of factory: {factory.print_product_class()}")



if __name__ == '__main__':
    print("FirstFactory")
    func(FirstFactory())

    print("SecondFactory")
    func(SecondFactory())





