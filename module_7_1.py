# Task "Учёт товаров"

from pprint import pprint

name = 'products.txt'

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}.')


class Shop(Product):

    def __init__(self, name, weight, category, __file_name = 'products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        file = open (self.__file_name, 'r')
        rd = file.read()
        print(f'{rd}')
        file.close()

    def add(self, *products):
        for i in products:
            p = (str(i))
            file = open(self.__file_name, 'r')
            j = file.read()
            file.close()
            if p not in j:
                file = open(self.__file_name, 'a')
                file.write(f'\n{p}')
                file.close()
            else:
                print(f'Продукт {p} уже есть в магазине')

s1 = Shop('',0,'')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')


print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())

