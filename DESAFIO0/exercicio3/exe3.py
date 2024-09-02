#definindo a função
def encontrar_subconjuntos(numeros):
    #começar com conjunto vazio
    subconjuntos = [[]]

    for numero in numeros:
        # Para cada número, é adicionado esse número a cada subconjunto existente
        subconjuntos += [subconjuntos_atual + [numero] for subconjuntos_atual in subconjuntos]

    return subconjuntos

# Exemplo de uso
numeros = [1, 2]
print(encontrar_subconjuntos(numeros))
