def merge_sort(lista):
  tamanho_lista = len(lista)
  
  if tamanho_lista > 1:
    meio = tamanho_lista // 2
    lista_esquerda = lista[:meio]
    lista_direita = lista[meio:]
    
    merge_sort(lista_esquerda)
    merge_sort(lista_direita)
    
    tamanho_lista_esquerda = len(lista_esquerda)
    tamanho_lista_direita = len(lista_direita)
    
    index_lista = 0
    index_lista_esquerda = 0
    index_lista_direita = 0
    
    while index_lista_esquerda < tamanho_lista_esquerda and index_lista_direita < tamanho_lista_direita:
      if lista_esquerda[index_lista_esquerda] < lista_direita[index_lista_direita]:
        lista[index_lista] = lista_esquerda[index_lista_esquerda]
        index_lista_esquerda += 1
      else:
        lista[index_lista] = lista_direita[index_lista_direita]
        index_lista_direita += 1
        
      index_lista += 1
      
    while index_lista_esquerda < tamanho_lista_esquerda:
      lista[index_lista] = lista_esquerda[index_lista_esquerda]
      index_lista_esquerda += 1
      index_lista += 1
      
    while index_lista_direita < tamanho_lista_direita:
      lista[index_lista] = lista_direita[index_lista_direita]
      index_lista_direita += 1
      index_lista += 1
      
      
