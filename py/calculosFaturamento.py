def calcular_menor_maior_faturamento(dados):
  """Calcula o menor e o maior valor de faturamento."""
  valores = [dia['valor'] for dia in dados if dia['valor'] > 0] 

  if not valores:
    print('Sem vendas para o período informado!')

  menor_valor = min(valores)
  maior_valor = max(valores)
  print(f'Menor faturamento: R$ {menor_valor:.2f}')
  print(f'Maior faturamento: R$ {maior_valor:.2f}')


def calcular_media_mensal(dados):
  """Calcula a média mensal de faturamento."""
  valores = [dia['valor'] for dia in dados if dia['valor'] > 0] 

  if not valores:
    print('Sem vendas para o período informado!')

  media = sum(valores) / len(valores)
  print(f'Média mensal de faturamento: R$ {media:.2f}')

  """Calcula o número de dias com faturamento acima da média."""
  dias_acima_media = sum(1 for dia in dados if dia['valor'] > media)
  print(f'Dias com faturamento acima da média: {dias_acima_media}')


def calcular_dias_sem_faturamento(dados):
  """Calcula o número de dias sem faturamento."""
  dias_sem_faturamento = sum(1 for dia in dados if dia['valor'] == 0)
  print(f'Dias sem faturamento: {dias_sem_faturamento}')

