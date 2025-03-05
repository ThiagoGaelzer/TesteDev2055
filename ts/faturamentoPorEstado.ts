// Dados de faturamento
const faturamento = {
    SP: 67836.43,
    RJ: 36678.66,
    MG: 29229.88,
    ES: 27165.48,
    Outros: 19849.53,
  };
  
  // Função para calcular o faturamento total
  function calcularFaturamentoTotal(dados: { [estado: string]: number }): number {
    let total = 0;
    for (const estado in dados) {
      if (dados.hasOwnProperty(estado)) {
        total += dados[estado];
      }
    }
    return total;
  }
  
  // Função para calcular o percentual de representação
  function calcularPercentual(
    faturamentoEstado: number,
    faturamentoTotal: number
  ): number {
    return (faturamentoEstado / faturamentoTotal) * 100;
  }
  
  // Calcular o faturamento total
  const faturamentoTotal = calcularFaturamentoTotal(faturamento);
  
  // Calcular e exibir os percentuais de representação
  console.log("Percentual de representação por estado:");
  for (const estado in faturamento) {
    if (faturamento.hasOwnProperty(estado)) {
      const percentual = calcularPercentual(faturamento[estado], faturamentoTotal);
      console.log(`${estado}: ${percentual.toFixed(2)}%`);
    }
  }