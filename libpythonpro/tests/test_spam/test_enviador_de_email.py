from libpythonpro.tests.spam.enviador_de_email import Enviador
import pytest

def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo2bar.com.br', 'renzo@python.pro.br']
    )
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.')

    assert destinatario in resultado