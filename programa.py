from quick_sort import quick_sort
from selection_sort import selection_sort

def main():
    lista = [4, 2, 1, 3, 0]
    quick_sort(lista)
    print("Lista ordenada com Quick Sort: ", end='')
    print(lista)
    
    lista = [4, 2, 1, 3, 0]
    selection_sort(lista)
    print("Lista ordenada com Selection Sort: ", end='')
    print(lista)
    
    
if __name__ == '__main__':
    main()