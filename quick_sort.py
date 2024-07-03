def quick_sort(lista, inicio = 0, fim=None):
    if fim is None:
        fim = len(lista) - 1
        
    if inicio < fim:
        pivo = divisao(lista, inicio, fim)
        quick_sort(lista, inicio, pivo - 1)
        quick_sort(lista, pivo + 1, fim)


def divisao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
            
    lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
    
    return esquerda