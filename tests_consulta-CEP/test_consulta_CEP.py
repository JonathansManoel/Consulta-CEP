import pytest
import consulta_CEP
from consulta_CEP import consulta_cep
import requests_mock
from unittest import mock


def test_func_consulta_cep():
    mock.patch('consulta_CEP.consulta_cep', return_value=consulta_cep)



# Tentando aprender como realizar testes!
# def test_consulta_cep_status_code():
#     consulta_cep.status_code == 200


# class TesteConsulta(consulta_cep):
#     @requests_mock.Mocker()
#     def test_status_code_200(self, r_mock):
#         url = 'https://viacep.com.br/ws/01001000/json/'
#         r_mock.get(url, status_code=200)
#         site = consulta_CEP.consulta_cep.r(url=url)
#         site.consulta_cep()
#         self.assertEqual(200, site.status)
