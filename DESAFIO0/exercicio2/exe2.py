def pares_menor_diferenca(array):
    # usando o 'sort' para ordenar o array efacilitar a comparação
    array.sort()

    # Inicializar a menor diferenca com valor alto
    menor_diferenca = float('inf')

    # Lista para armazenar os pares com menor diferença
    pares_com_menor_diferenca = []

    # Loop para encontar as diferenças entre os números consecutivos
    for i in range(len(array) - 1):
        #calcula a diferença entre números consecutivos
        diferenca = array[i + 1] - array[i]

        # se encontrar uma diferença menor, atualizar a menor diferença
        # então inicia uma lista de pares
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            pares_com_menor_diferenca = [(array[i], array[i + 1])]

        # se encontrar a mesma menor diferença , adiciona o par À lista
        elif diferenca == menor_diferenca:
            pares_com_menor_diferenca.append((array[i], array[i + 1]))

    #Retorna a lista de pares com a menor diferença
    return pares_com_menor_diferenca

# uso 
array = [7, 5, 4, 6, 8, 10, 9, 13]
resultado = pares_menor_diferenca(array)
print(resultado)