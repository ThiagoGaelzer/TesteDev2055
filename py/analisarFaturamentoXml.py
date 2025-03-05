import os
from calculosFaturamento import *

def ler_dados_faturamento_xml(nome_arquivo):
    """Lê os dados de faturamento de um arquivo XML"""
    caminho_arquivo = os.path.join('database', nome_arquivo)
    dados = []
    with open(caminho_arquivo, 'r') as arquivo:
        linha = arquivo.readline()
        while linha:
            if '<row>' in linha:
                dia_linha = arquivo.readline().strip()
                valor_linha = arquivo.readline().strip()
                arquivo.readline()  

                dia = int(dia_linha.split('>')[1].split('<')[0])
                valor = float(valor_linha.split('>')[1].split('<')[0])
                dados.append({'dia': dia, 'valor': valor})
            linha = arquivo.readline()
    return dados

dados_faturamento = ler_dados_faturamento_xml('dados.xml')

"""Chamada das funções de cálculo"""
calcular_menor_maior_faturamento(dados_faturamento)
calcular_media_mensal(dados_faturamento)
calcular_dias_sem_faturamento(dados_faturamento)
