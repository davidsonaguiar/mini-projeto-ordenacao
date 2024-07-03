def selection_sort(lista):
    tamanho_lista = len(lista)
 
    for index_posicao_busca in range(tamanho_lista - 1):
        index_menor_valor = index_posicao_busca
        
        for index_for in range(index_posicao_busca, tamanho_lista):
            if lista[index_for] < lista[index_menor_valor]:
                index_menor_valor = index_for
                
        if lista[index_posicao_busca] > lista[index_menor_valor]:
            lista[index_posicao_busca], lista[index_menor_valor] = lista[index_menor_valor], lista[index_posicao_busca]
            
        
    
    