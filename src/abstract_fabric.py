from abc import ABC, abstractmethod


class Product(ABC):
    # Наследуем от Product, в случае если нам понадобится общая реализация метода для детей Product
    pass


class Chair(Product):
    pass

class Table(Product):
    pass

class FirstChair(Chair):
    pass

class SecondChair(Chair):
    pass

class FirstTable(Table):
    pass

class SecondTable(Table):
    pass


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) ->Table:
        pass


class FirstFactory(AbstractFactory):
    def create_chair(self) -> FirstChair:
        return FirstChair()

    def create_table(self) -> FirstTable:
        return FirstTable()


class SecondFactory(AbstractFactory):
    def create_chair(self) -> SecondChair:
        return SecondChair()

    def create_table(self) -> SecondTable:
        return SecondTable()


def func(factory: AbstractFactory):
    chair = factory.create_chair()
    table = factory.create_table()

    print(f"Chair is {chair.__class__}")
    print(f"Table is {table.__class__}")


def main():
    """
    Мне не совсем понятно для чего на refactoring guru реализуют отдельные методы,
    которые взаимодействуют только с объектами такого же типа. Мне кажется для примера эта логика избыточна, поэтому оставляю это здесь
    Если будут какие-то вопросы или поправки. Жду PR
    """

    func(FirstFactory())
    func(SecondFactory())


    """
    Вывод следующий: 
        Chair is <class '__main__.FirstChair'>
        Table is <class '__main__.FirstTable'>
        Chair is <class '__main__.SecondChair'>
        Table is <class '__main__.SecondTable'>
    Откуда можно сделать вывод что фабрика создаёт объекты нужных нам типов при запросе
    """

if __name__ == '__main__':
    main()

