import meu_modulo

print(f"O nome é {meu_modulo.NOME}")

meu_modulo.funcao1()


import meu_modulo as mm

mm.funcao2()

"""
O python cria modulos como singleton assim não deixando importar varias vezes a mesma classe
"""
