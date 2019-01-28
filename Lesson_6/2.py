"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof


class Person():
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def surname(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Person1():
    __slots__ = ['name','job','pay']
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def surname(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


class Departament:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRises(self, percent):
        for pers in self.members:
            pers.giveRises(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':  # Тестирование.
    bob = Person('Bob Smith')
    sue = Person('Suy Jones', job='dev', pay=100000)
    bob_2 = Person1('Bob Smith')
    sue_2 = Person1('Suy Jones', job='dev', pay=100000)
    print('Размер экземпляра класса {} без использования слотов {} bytes'.format(bob.name,asizeof.asizeof(bob)))
    print('Размер экземпляра класса {} c  использованием слотов {} bytes'.format(bob_2.name,asizeof.asizeof(bob_2)))
    print('Размер экземпляра класса {} без использования слотов {} bytes'.format(sue.name,asizeof.asizeof(sue)))
    print('Размер экземпляра класса {} с  использованием слотов {} bytes'.format(sue_2.name,asizeof.asizeof(sue_2)))

'''
Windows 10, 64-бит
Python 3.7

Размер экземпляра класса Bob Smith без использования слотов 264 bytes
Размер экземпляра класса Bob Smith c  использованием слотов 104 bytes
Размер экземпляра класса Suy Jones без использования слотов 288 bytes
Размер экземпляра класса Suy Jones с  использованием слотов 128 bytes
'''


'''
    # print(bob.name, bob.job, bob.pay)
    # print(sue.surname(), sue.job, sue.pay)
    # sue.giveRaise(.10)
    # print(sue.pay)
    # print(bob.surname())
    bob.giveRaise(15)
    print(sue)
    print(bob)
    tom = Manager('Tom Jones', 50000)
    print(tom)
    tom.giveRaise(0.1)
    print(tom)
    print(tom.surname())
    print('--All three--')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)
    development = Departament(bob, sue)
    development.addMember(tom)
    development.showAll()
    for key in bob.__dict__:
        print(key, '=>', getattr(bob, key))
'''