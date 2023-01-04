class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print('Criando Objecto')
        return cls.instance


s1 = Singleton()
print(f'Instancia 1 {id(s1)}')

s2 = Singleton()
print(f'Instancia 2 {id(s2)}')
