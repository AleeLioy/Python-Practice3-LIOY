def concatena(string1, string2, nro):
    concatenado = string1 + string2
    resultado = concatenado * nro
    return resultado

# Ejemplo
string1 = "Hola, "
string2 = "mundo!"
nro = 3

resultado = concatena(string1, string2, nro)
print(resultado)
