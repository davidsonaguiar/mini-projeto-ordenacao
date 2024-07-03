from selection_sort import selection_sort
from teste.mensurador import mensurador

def selection_sort_teste(dados, resultados):
    tempo = mensurador(selection_sort, dados)
    resultados['Selection Sort'].append(tempo)
    print(f"Selection Sort: {tempo:.5f} segundos")