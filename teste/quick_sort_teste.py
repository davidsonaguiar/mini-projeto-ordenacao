from quick_sort import quick_sort
from teste.mensurador import mensurador

def quick_sort_teste(dados, resultados):
    tempo = mensurador(quick_sort, dados)
    resultados["Quick Sort"].append(tempo)
    print(f"Quick Sort: {tempo:.5f} segundos")