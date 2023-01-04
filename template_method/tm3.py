from abc import ABCMeta, abstractmethod


class Viagem(metaclass=ABCMeta):
    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass

    @abstractmethod
    def retorno(self):
        pass

    def itinerario(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retorno()


class ViagemVeneza(Viagem):

    def ida(self):
        print('Viagem de avião...')

    def dia1(self):
        print('Visita a Basilica de São Marcos na Preça São Marcos')

    def dia2(self):
        print('Visita ao Palaico Doge')

    def dia3(self):
        print('Aproveitar a comida próximo à ponte Rialto')

    def retorno(self):
        print('Viagem de Avião...')


class ViagemMalvinas(Viagem):
    def ida(self):
        print('Viagem de onibus...')

    def dia1(self):
        print('Apreciar a vida marinha de Banana Reef')

    def dia2(self):
        print('Praticar esportes aquátivos')

    def dia3(self):
        print('Relaxar na praia e aproveitar o sol')

    def retorno(self):
        print('Viagem de avião...')


class GeekTravel:
    def preparar_viagem(self):
        opcao = input('Qual local de viagem deseja fazer? [Veneza, Malvinas]')
        if opcao == 'Veneza':
            self.viagem = ViagemVeneza()
            self.viagem.itinerario()
        elif opcao == 'Malvinas':
            self.viagem = ViagemMalvinas()
            self.viagem.itinerario()
        else:
            print('Opção inválida')


if __name__ == '__main__':
    agencia = GeekTravel()
    agencia.preparar_viagem()
