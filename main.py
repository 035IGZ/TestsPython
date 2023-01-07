from codigo.bytebank import Funcionario

lucas = Funcionario('Lucas Iglezias', '03/05/2002', 1000)

print(lucas.idade())


def teste_idade():
    funcionario_test = Funcionario('Teste', '03/05/2002', 1111)
    print(f'Teste = {funcionario_test.idade}')


ana = Funcionario('Ana', '11/11/1111', 1000)

print(ana.calcular_bonus())
