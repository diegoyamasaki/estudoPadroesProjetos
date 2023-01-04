from abc import ABCMeta, abstractmethod


class ClassAbstrata(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operacao1(self):
        pass

    @abstractmethod
    def operacao2(self):
        pass

    def template_method(self):
        print('Definindo o algoritmo: Operação 1 após Operação 2')
        self.operacao2()
        self.operacao1()


class ClasseConcreta(ClassAbstrata):

    def operacao1(self):
        print('Minha operação concreta 1')

    def operacao2(self):
        print('Minha operação concreta 2')


class Cliente:
    def main(self):
        self.concreta = ClasseConcreta()
        self.concreta.template_method()


if __name__ == '__main__':
    cliente = Cliente()
    cliente.main()

