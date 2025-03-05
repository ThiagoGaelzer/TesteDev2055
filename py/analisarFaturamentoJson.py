import json
import os
from calculosFaturamento import *

def ler_dados_faturamento(nome_arquivo):
  """Lê os dados de faturamento de um arquivo JSON."""
  caminho_arquivo = os.path.join('database', nome_arquivo)
  with open(caminho_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)
  return dados

dados_faturamento = ler_dados_faturamento('dados.json')

"""Chamada das funções de cálculo"""
calcular_menor_maior_faturamento(dados_faturamento)
calcular_media_mensal(dados_faturamento)
calcular_dias_sem_faturamento(dados_faturamento)
