from abc import ABCMeta, abstractmethod


class Compilador(metaclass=ABCMeta):

    @abstractmethod
    def coletar_fonte(self):
        pass

    @abstractmethod
    def compilar_objeto(self):
        pass

    @abstractmethod
    def executar(self):
        pass

    def compilar_e_executar(self):
        self.coletar_fonte()
        self.compilar_objeto()
        self.executar()


class CompiladorIOS(Compilador):

    def coletar_fonte(self):
        print('IOS :: Coletando codigo fonte Swift')

    def compilar_objeto(self):
        print('IOS :: Compilando codigo Swift')

    def executar(self):
        print('IOS :: programa executando no ambiente de execução')


class CompiladorAndroid(Compilador):

    def coletar_fonte(self):
        print('ANDROID :: Coletando codigo fonte Kotlin')

    def compilar_objeto(self):
        print('ANDROID :: Compilando codigo Kotlin para bytecode JVM')

    def executar(self):
        print('ANDROID :: programa executando no ambiente de execução')


if __name__ == '__main__':
    ios = CompiladorIOS()
    ios.compilar_e_executar()
    android = CompiladorAndroid()
    android.compilar_e_executar()

