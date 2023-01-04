# Façade

class GerenciamentoEventos:

    def __init__(self):
        self.salao = None
        self.florista = None
        self.comida = None
        self.musica = None
        print('GerenciamnetoEeventos :: Vou organizar com todo mundo!\n\n')

    def organizar(self):
        self.salao = SalaoFesta()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()


# SubSistema 1
class SalaoFesta:
    def __init__(self):
        print('SalaoFesta :: Agendando o salão de festas para o casamento....')

    def _esta_disponivel(self):
        print('SalaoFestas :: Este salão de festas está disponivel ?')
        return True

    def agendar(self):
        if self._esta_disponivel():
            print('SalaoFestas :: Agendamento do salão realizado\n')


# SubSistema 2
class Florista:
    def __init__(self):
        print('Florista :: Flores para um evento ?')

    def arranjar_flores(self):
        print('Florista :: Rosas, Margaridas e Lirios serão usados... \n')


# SubSistema 3
class Restaurante:
    def __init__(self):
        print('Restaurante :: Comida para eventos...')

    def preparar(self):
        print('Restaurante :: Comida chinesa e brasileira serão servidos...\n')


# SubSistema 4
class Banda:
    def __init__(self):
        print('Banda :: Arranjos musicais para o evento...')

    def montar_palco(self):
        print('Banda :: Preparando o palco para tocar jazz e rock no evento.\n')


# Cliente
class Cliente:
    def __init__(self):
        print('Cliente :: Uau! Preparação para o casamento')

    def contrata_gerente_eventos(self):
        print('Cliente :: Vou contratar uma empresa para gerenciar eventos\n')
        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print('Cliente :: Foi muito simples organizar esete evento com o Facade')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.contrata_gerente_eventos()
