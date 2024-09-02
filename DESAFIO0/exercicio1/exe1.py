
def gerador_asteriscos(n):
    #cria uma lista vazia para poder armazenar as strings
    lista_asteriscos = []

    # loop para gerar as strings
    for i in range(1, n + 1):
        #cria asterisco com i asterisco
        asteriscos = '*' * i
        #adicionando a string na lista com append
        lista_asteriscos.append(asteriscos)

        #retornando resultado da lista
    return lista_asteriscos
    
    #uso da função
resultado = gerador_asteriscos(5)
print(resultado)


