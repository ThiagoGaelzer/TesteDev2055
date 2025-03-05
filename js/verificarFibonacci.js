function verificarFibonacci(numero) {
    let a = 0;
    let b = 1;
    let fibonacci = [a, b];
  
    while (b <= numero) {
      if (b === numero) {
        return `${numero} pertence à sequência de Fibonacci: ${fibonacci.join(', ')}`;
      }
      const temp = b;
      b = a + b;
      a = temp;
      fibonacci.push(b);
    }
    return `${numero} não pertence à sequência de Fibonacci: ${fibonacci.join(', ')}`;
  }
  
  console.log(verificarFibonacci(8)); 
  console.log(verificarFibonacci(10)); 