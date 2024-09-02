from typing import List, Tuple

def encontrar_menor_diferenca(
    numeros: List[int],
    permitir_duplicatas: bool = True,
    pares_ordenados: bool = False,
    pares_unicos: bool = False
) -> List[Tuple[int, int]]:
    # Ordena a lista de números para facilitar a busca pelas menores diferenças
    numeros.sort()

    # Inicializa a lista de pares e define a menor diferença inicial como um número muito grande
    pares = []
    menor_diferenca = float('inf')

    # Percorre o array comparando cada número com os seguintes
    for i in range(len(numeros) - 1):
        diferenca = abs(numeros[i] - numeros[i + 1])
        
        # Se encontrar uma diferença menor, atualiza a menor diferença e reinicia a lista de pares
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            pares = [(numeros[i], numeros[i + 1])]
        # Se encontrar a mesma diferença mínima, adiciona o par à lista
        elif diferenca == menor_diferenca:
            pares.append((numeros[i], numeros[i + 1]))

    # Se permitir_duplicatas for False, remove pares com números iguais
    if not permitir_duplicatas:
        pares = [(a, b) for a, b in pares if a != b]

    # Se pares_ordenados for True, ordena cada par internamente
    if pares_ordenados:
        pares = [(min(a, b), max(a, b)) for a, b in pares]

    # Se pares_unicos for True, remove pares duplicados
    if pares_unicos:
        pares = list(set((min(a, b), max(a, b)) for a, b in pares))

    return pares

# Teste da função com um exemplo
numeros = [1, 3, 4, 7, 10, 20, 2]
resultado = encontrar_menor_diferenca(numeros, permitir_duplicatas=False, pares_ordenados=True, pares_unicos=True)
print(resultado)