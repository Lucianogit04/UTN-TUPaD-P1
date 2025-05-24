def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 caracter, es palíndromo
    if len(palabra) <= 1:
        return True
    
    # Verificamos si el primer y último carácter son iguales
    if palabra[0] != palabra[-1]:
        return False
    
    # Llamada recursiva con la subcadena sin el primer y último carácter
    return es_palindromo(palabra[1:-1])


if __name__ == "__main__":

    print(es_palindromo("ana"))      
    print(es_palindromo("oso"))      
    print(es_palindromo("python"))   
    print(es_palindromo("radar"))    
    print(es_palindromo(""))        
    print(es_palindromo("a"))       
