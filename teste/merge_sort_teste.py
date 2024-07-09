from merge_sort import merge_sort
from teste.mensurador import mensurador

def merge_sort_teste(dados, resultados):
  tempo = mensurador(merge_sort, dados)
  resultados["Merge Sort"].append(tempo)
  print(f"Merge Sort: {tempo:.5f} segundos")