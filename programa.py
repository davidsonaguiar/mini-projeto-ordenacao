from quick_sort import quick_sort
from selection_sort import selection_sort
from hybrid_sort import hybrid_sort

def main():
    print()
    lista = [12, 4, 5, 6, 7, 3, 1, 15, 10, 2, 8, 9, 14, 13, 11]
    quick_sort(lista)
    print("Lista ordenada com Quick Sort: ")
    print(lista)
    print()
    
    lista = [12, 4, 5, 6, 7, 3, 1, 15, 10, 2, 8, 9, 14, 13, 11]
    selection_sort(lista)
    print("Lista ordenada com Selection Sort: ")
    print(lista)
    print()
    
    lista = [12, 4, 5, 6, 2, 8, 9, 14, 7, 3, 1, 15, 10, 13, 11]
    hybrid_sort(lista)
    print("Lista ordenada com Hybrid Sort: ")
    print(lista)
    print()
    
    
if __name__ == '__main__':
    main()