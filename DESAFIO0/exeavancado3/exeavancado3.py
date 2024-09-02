from typing import List

def encontrar_subconjuntos(
    conjunto: List[int],
    max_tamanho: int = None,
    min_tamanho: int = 0,
    somente_distintos: bool = False,
    ordenar_subconjuntos: bool = False
) -> List[List[int]]:
    # Função para gerar todos os subconjuntos
    def gerar_subconjuntos(nums):
        subconjuntos = [[]]  # Começa com o subconjunto vazio
        for num in nums:
            # Para cada elemento, adiciona ele a todos os subconjuntos existentes
            novos_subconjuntos = [sub + [num] for sub in subconjuntos]
            subconjuntos.extend(novos_subconjuntos)
        return subconjuntos

    # Remove duplicatas se solicitado
    if somente_distintos:
        conjunto = list(set(conjunto))  # Converte para set para remover duplicatas e volta para lista

    # Gera todos os subconjuntos
    todos_subconjuntos = gerar_subconjuntos(conjunto)

    # Filtra por tamanho mínimo e máximo
    subconjuntos_filtrados = [
        sub for sub in todos_subconjuntos 
        if (min_tamanho <= len(sub)) and (max_tamanho is None or len(sub) <= max_tamanho)
    ]

    # Ordena subconjuntos e seus elementos se solicitado
    if ordenar_subconjuntos:
        subconjuntos_filtrados = [sorted(sub) for sub in subconjuntos_filtrados]
        subconjuntos_filtrados.sort(key=len)

    return subconjuntos_filtrados

# Testando a função
conjunto = [1, 2, 2, 3]
resultado = encontrar_subconjuntos(conjunto, max_tamanho=3, min_tamanho=1, somente_distintos=True, ordenar_subconjuntos=True)
print(resultado)
