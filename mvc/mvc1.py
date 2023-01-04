class Modelo:
    def __init__(self):
        self.produtos = {
            'ps5': {'id': 1, 'nome': 'playstation 5', 'preco': 1244},
            'xbox': {'id': 2, 'nome': 'xbox', 'preco': 1644},
            'switch': {'id': 3, 'nome': 'switch', 'preco': 944}
        }


class Controlador:
    def __init__(self):
        self.modelo = Modelo()

    def listar_produtos(self):
        produtos = self.modelo.produtos.keys()

        print('-------------PRODUTOS-----------------')
        for chave in produtos:
            print(f'iD: {self.modelo.produtos[chave]["id"]}')
            print(f'Nome: {self.modelo.produtos[chave]["nome"]}')
            print(f'Preço: {self.modelo.produtos[chave]["preco"]}')
            print('')


class Visao:

    def __init__(self):
        self.controlador = Controlador()

    def produtos(self):
        self.controlador.listar_produtos()


if __name__ == '__main__':
    visao = Visao()
    visao.produtos()

