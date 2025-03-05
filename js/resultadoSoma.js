function calcularSoma(indice) {
    let soma = 0;
    let k = 0;
  
    while (k < indice) {
      k = k + 1;
      soma = soma + k;
    }
  
    return soma;
  }
  
  let resultado = calcularSoma(13);
  console.log("Resultado = "+resultado);