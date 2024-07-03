def hybrid_sort(lista, inicio = 0, fim=None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio < fim:
        if (fim - inicio) < 10:
            return selection_sort_sublist(lista, inicio, fim)
        pivo = divisao(lista, inicio, fim)
        hybrid_sort(lista, inicio, pivo - 1)
        hybrid_sort(lista, pivo + 1, fim)


def selection_sort_sublist(lista, inicio, fim):
    for index_posicao_busca in range(inicio, fim):
        index_menor_valor = index_posicao_busca
        
        for index_for in range(index_posicao_busca, fim + 1):
            if lista[index_for] < lista[index_menor_valor]:
                index_menor_valor = index_for
                
        if lista[index_posicao_busca] > lista[index_menor_valor]:
            lista[index_posicao_busca], lista[index_menor_valor] = lista[index_menor_valor], lista[index_posicao_busca]
            

def divisao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
            
    lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
    
    return esquerda