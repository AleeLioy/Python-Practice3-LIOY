def primeros_tres(lista):
    if len(lista) >= 3:
        return lista[:3]
    else:
        return lista

# Ejemplo
lista = ["ho", 3.16, "la", 81, 6, 42]
resultado = primeros_tres(lista)
print(resultado)
