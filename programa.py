from teste.gerador_dados import gerador_dados
from teste.selection_sort_teste import selection_sort_teste
from teste.quick_sort_teste import quick_sort_teste   
from teste.hybrid_sort_teste import hybrid_sort_teste
from teste.merge_sort_teste import merge_sort_teste
    
if __name__ == '__main__':
    tamanhos = [1000, 10000, 50000, 500000]
    results = {
        'Selection Sort': [],
        'Quick Sort': [],
        'Merge Sort': [],
        'Hybrid Sort (limite=16)': [],
        'Hybrid Sort (limite=64)': [],
        'Hybrid Sort (limite=256)': []
    }
    
    for tamanho in tamanhos:
        data = gerador_dados(tamanho)
        print(f"Iniciado o teste com o tamanho de dados: {tamanho}")
        
        data_copy = data.copy()
        quick_sort_teste(data_copy, results)
        
        data_copy = data.copy()
        hybrid_sort_teste(data_copy, results, 16)
        
        data_copy = data.copy()
        hybrid_sort_teste(data_copy, results, 64)
        
        data_copy = data.copy()
        hybrid_sort_teste(data_copy, results, 256)
        
        data_copy = data.copy()
        merge_sort_teste(data_copy, results)
        
        data_copy = data.copy()
        selection_sort_teste(data_copy, results)
        
        print()
    
    
    for algoritmo, tempo in results.items():
        print(f"{algoritmo}: {tempo}")