from typing import List, Tuple


class Curso:

    def __init__(self: object, nome: str = 'Curso Padrão', carga_horaria: int = 45) -> None:
        self.__nome = nome
        self.__carga_horario = carga_horaria


curso1: Curso = Curso()
curso2: Curso = Curso(nome='Padrões de projeto em Python')
curso3: Curso = Curso(nome='Orquestração de Containers com Kubernetes', carga_horaria=23)

# print(curso1.__dict__)
# print(curso2.__dict__)
# print(curso3.__dict__)

nome: str = "Geek University"
tupla: Tuple = (1, 2, 3, 4, 5)
lista: List = [1, 2, 3, 4, 5]


# print(nome[:4], tupla[:4], lista[:4])


class Pessoa:

    def __init__(self: object, nome: str) -> None:
        self.__nome = nome

    def andar(self: object) -> None:
        print('Estou andando...')


class Aluno(Pessoa):

    def __init__(self: object, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.__matricula = matricula


felicity = Aluno('Felicity', '12345')


# felicity.andar()


def gerar_fibonacci(quantidade: int) -> None:
    if quantidade <= 0:
        print('A quantidade deve ser maior que 0')
    else:
        print(f'A sequência fibonacci para {quantidade} termo(s) é: ')
        contador: int = 0
        aux1: int = 0
        aux2: int = 1
        while contador < quantidade:
            print(aux1)
            proximo = aux1 + aux2
            aux1 = aux2
            aux2 = proximo
            contador += 1


# gerar_fibonacci(10)

class Motor:

    def ligar(self: object) -> None:
        print('Motor ligado...')


class Pneu:

    def encher(self: object):
        print('Pneu cheio')


class Carro:

    def __init__(self: object, modelo: str):
        self.__modelo = modelo
        self.__motor = Motor()
        self.pneu1 = Pneu()
        self.pneu2 = Pneu()
        self.pneu3 = Pneu()
        self.pneu4 = Pneu()

fusca = Carro('Fusca')
fusca._Carro__motor.ligar()
