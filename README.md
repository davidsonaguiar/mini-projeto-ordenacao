### Relatório de Desempenho

#### 1. Descrição do Algoritmo Híbrido

**Detalhes sobre a Implementação:**

- **Seleção do Pivô:** 
  O algoritmo híbrido utiliza o QuickSort como base. O pivô é escolhido como o último elemento da sub-lista em cada chamada recursiva da função `divisao`.

- **Divisão e Conquista:** 
  A lista é particionada em sub-listas menores com base no pivô selecionado. Os elementos menores ou iguais ao pivô são movidos para a esquerda, e os elementos maiores são movidos para a direita.

- **Aplicação do SelectionSort:** 
  Quando o tamanho da sub-lista é menor que 10, o algoritmo híbrido aplica o SelectionSort para ordenar a sub-lista. A função `selection_sort_sublist` é responsável por essa tarefa.

- **Combinação das Sub-listas:** 
  Após as sub-listas serem ordenadas, elas são combinadas para formar a lista final ordenada. A função `hybrid_sort` chama recursivamente a si mesma para ordenar as sub-listas menores até que todas estejam ordenadas.

**Análise de Desempenho:**

- **Melhor Caso:** O pivô sempre divide a lista em duas metades iguais, resultando em uma complexidade de \(O(n \log n)\).

- **Caso Médio:** O pivô divide a lista em partes aproximadamente iguais, resultando em uma complexidade de \(O(n \log n)\).

- **Pior Caso:** O pivô é sempre o menor ou o maior elemento, resultando em uma complexidade de \(O(n^2)\). No entanto, a aplicação do SelectionSort para sub-listas menores ajuda a melhorar o desempenho em casos de listas pequenas.

#### 2. Metodologia do Teste de Desempenho

**Conjuntos de Dados Usados:**

- Conjunto de Dados Muito Pequeno: 1.000 elementos
- Conjunto de Dados Pequeno: 10.000 elementos
- Conjunto de Dados Médio: 50.000 elementos
- Conjunto de Dados Grande: 500.000 elementos

**Procedimento para Medir o Tempo de Execução dos Algoritmos:**

- Para garantir uma comparação justa e precisa, a lista de dados foi gerada uma única vez para cada tamanho e copiada antes de cada execução de um algoritmo de ordenação.
- O tempo de execução foi medido utilizando a função `time.time()` do Python.
- Cada algoritmo foi executado em cada conjunto de dados, e o tempo de execução foi registrado.

**Número de Repetições dos Testes:**

- Cada teste foi realizado quatro vez.

#### 3. Resultados do Teste de Desempenho

**Tabelas e Gráficos:**

### Tamanho dos Dados: 1000

| Algoritmo                | Teste 1 (s) | Teste 2 (s) | Teste 3 (s) | Teste 4 (s) | Média (s)    |
|--------------------------|-------------|-------------|-------------|-------------|--------------|
| Quick Sort               | 0.00000     | 0.00000     | 0.00000     | 0.00098     | 0.00025      |
| Hybrid Sort (limite=16)  | 0.00000     | 0.00000     | 0.00000     | 0.00100     | 0.00025      |
| Hybrid Sort (limite=64)  | 0.00000     | 0.00000     | 0.00000     | 0.00051     | 0.00013      |
| Hybrid Sort (limite=256) | 0.00000     | 0.00000     | 0.00000     | 0.00107     | 0.00027      |
| Merge Sort               | 0.00000     | 0.00000     | 0.00000     | 0.00100     | 0.00025      |
| Selection Sort           | 0.02049     | 0.01716     | 0.01653     | 0.01254     | 0.01668      |

### Tamanho dos Dados: 10000

| Algoritmo                | Teste 1 (s) | Teste 2 (s) | Teste 3 (s) | Teste 4 (s) | Média (s)    |
|--------------------------|-------------|-------------|-------------|-------------|--------------|
| Quick Sort               | 0.00000     | 0.00697     | 0.01234     | 0.00764     | 0.00674      |
| Hybrid Sort (limite=16)  | 0.01424     | 0.00529     | 0.01153     | 0.00969     | 0.01069      |
| Hybrid Sort (limite=64)  | 0.00303     | 0.00884     | 0.00485     | 0.00405     | 0.00519      |
| Hybrid Sort (limite=256) | 0.01021     | 0.00772     | 0.01273     | 0.00984     | 0.01013      |
| Merge Sort               | 0.00826     | 0.00238     | 0.01059     | 0.00198     | 0.00580      |
| Selection Sort           | 1.10239     | 1.13255     | 1.06202     | 1.08698     | 1.09599      |

### Tamanho dos Dados: 50000

| Algoritmo                | Teste 1 (s) | Teste 2 (s) | Teste 3 (s) | Teste 4 (s) | Média (s)    |
|--------------------------|-------------|-------------|-------------|-------------|--------------|
| Quick Sort               | 0.03609     | 0.03793     | 0.04219     | 0.04693     | 0.04029      |
| Hybrid Sort (limite=16)  | 0.04247     | 0.04288     | 0.04977     | 0.04986     | 0.04624      |
| Hybrid Sort (limite=64)  | 0.03509     | 0.04978     | 0.04820     | 0.03284     | 0.04198      |
| Hybrid Sort (limite=256) | 0.05037     | 0.03386     | 0.03683     | 0.05019     | 0.04281      |
| Merge Sort               | 0.05037     | 0.06599     | 0.04735     | 0.04660     | 0.05208      |
| Selection Sort           | 27.62893    | 28.36534    | 27.76078    | 27.76450    | 27.87989     |

### Tamanho dos Dados: 500000

| Algoritmo                | Teste 1 (s) | Teste 2 (s) | Teste 3 (s) | Teste 4 (s) | Média (s)    |
|--------------------------|-------------|-------------|-------------|-------------|--------------|
| Quick Sort               | 0.50924     | 0.56519     | 0.52792     | 0.52802     | 0.53209      |
| Hybrid Sort (limite=16)  | 0.53138     | 0.59971     | 0.53337     | 0.52732     | 0.54795      |
| Hybrid Sort (limite=64)  | 0.54567     | 0.53257     | 0.56339     | 0.52289     | 0.54163      |
| Hybrid Sort (limite=256) | 0.53109     | 0.55002     | 0.53345     | 0.52789     | 0.53511      |
| Merge Sort               | 0.67206     | 0.70021     | 0.68877     | 0.68979     | 0.68721      |

#### 4. Discussão dos Resultados

**Comparação do Desempenho do Algoritmo Híbrido com os Outros Algoritmos:**

- **Quick Sort:** Demonstrou um desempenho consistentemente rápido em todos os tamanhos de dados. O tempo de execução foi o mais curto, especialmente em tamanhos maiores.

- **Merge Sort:** Também apresentou bom desempenho, especialmente em dados maiores, mas geralmente foi mais lento que o QuickSort.

- **Selection Sort:** Muito mais lento que os outros algoritmos, especialmente em conjuntos de dados maiores. Não é adequado para grandes volumes de dados.

- **Algoritmo Híbrido (limite=16):** Teve desempenho próximo ao QuickSort em tamanhos menores, mas ficou atrás em conjuntos de dados maiores.

- **Algoritmo Híbrido (limite=64):** Mostrou um desempenho melhor em conjuntos de dados pequenos e médios, mas não foi significativamente melhor que o QuickSort.

- **Algoritmo Híbrido (limite=256):** Teve um desempenho similar ao limite de 64, com uma ligeira vantagem em tamanhos de dados muito grandes.
