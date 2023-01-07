from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '03/05/2002'  # Given-Contexto
        esperado = 21

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_lucas_iglezias_deve_retornar_apenas_iglezias(self):
        entrada = 'Lucas Iglezias'
        esperado = 'Iglezias'

        funcionario_teste = Funcionario(entrada, '03/05/2002', 1111)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Lucas Iglezias'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # Given
        esperado = 100

        funcionario_teste = Funcionario('Teste', '03/05/2002', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recece_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # Given

            funcionario_teste = Funcionario('Teste', '03/05/2002', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado  # then

    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Teste', '11/11/1111', 1000  # Given
        esperado = 'Funcionario(Teste, 11/11/1111, 1000)'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()

        assert resultado == esperado
