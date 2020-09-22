<<<<<<< HEAD
import pytest

=======
>>>>>>> 3be0054... Implementada Implementação de Conexão, Sessão e Usuário.
from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


<<<<<<< HEAD
@pytest.fixture
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(conexao, sessao):
=======
def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
>>>>>>> 3be0054... Implementada Implementação de Conexão, Sessão e Usuário.
    usuarios = [Usuario(nome='Renzo'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
<<<<<<< HEAD
=======
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
>>>>>>> 3be0054... Implementada Implementação de Conexão, Sessão e Usuário.
