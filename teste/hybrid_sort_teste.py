from hybrid_sort import hybrid_sort
from teste.mensurador import mensurador

def hybrid_sort_teste(dados, resultado, limite):
    tempo = mensurador(hybrid_sort, dados, limite)
    resultado[f"Hybrid Sort (limite={limite})"].append(tempo)
    print(f"Hybrid Sort (limite={limite}): {tempo:.5f} segundos")