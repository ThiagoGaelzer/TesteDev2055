function inverterString(str: string): string {
    // Converte a string em um array de caracteres
    let caracteres: string[] = str.split(''); 
    let stringInvertida: string = '';

    //Itera sobre a String de trás para frente
    for (let i = caracteres.length - 1; i >= 0; i--) { 
        stringInvertida += caracteres[i]; 
    }

    return stringInvertida;
}

let stringOriginal: string = "Texto de exemplo";
let stringInvertida: string = inverterString(stringOriginal);
console.log(stringInvertida); 
