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

- Cada teste foi realizado uma vez devido ao tempo de execução limitado.

#### 3. Resultados do Teste de Desempenho

**Tabelas e Gráficos:**

| Tamanho dos Dados | Algoritmo                | Tempo Médio (s) |
|-------------------|--------------------------|-----------------|
| 1000              | Quick Sort               | 0.00000         |
| 1000              | Hybrid Sort (limite=16)  | 0.00000         |
| 1000              | Hybrid Sort (limite=64)  | 0.00000         |
| 1000              | Hybrid Sort (limite=256) | 0.00000         |
| 1000              | Merge Sort               | 0.00000         |
| 1000              | Selection Sort           | 0.02049         |
| 10000             | Quick Sort               | 0.00000         |
| 10000             | Hybrid Sort (limite=16)  | 0.01424         |
| 10000             | Hybrid Sort (limite=64)  | 0.00303         |
| 10000             | Hybrid Sort (limite=256) | 0.01021         |
| 10000             | Merge Sort               | 0.00826         |
| 10000             | Selection Sort           | 1.10239         |
| 50000             | Quick Sort               | 0.03609         |
| 50000             | Hybrid Sort (limite=16)  | 0.04247         |
| 50000             | Hybrid Sort (limite=64)  | 0.03509         |
| 50000             | Hybrid Sort (limite=256) | 0.05037         |
| 50000             | Merge Sort               | 0.05037         |
| 50000             | Selection Sort           | 27.62893        |
| 500000            | Quick Sort               | 0.50924         |
| 500000            | Hybrid Sort (limite=16)  | 0.53138         |
| 500000            | Hybrid Sort (limite=64)  | 0.54567         |
| 500000            | Hybrid Sort (limite=256) | 0.53109         |
| 500000            | Merge Sort               | 0.67206         |
| 500000            | Selection Sort           | >600            |

#### 4. Discussão dos Resultados

**Comparação do Desempenho do Algoritmo Híbrido com os Outros Algoritmos:**

- **Quick Sort:** Demonstrou um desempenho consistentemente rápido em todos os tamanhos de dados. O tempo de execução foi o mais curto, especialmente em tamanhos maiores.

- **Merge Sort:** Também apresentou bom desempenho, especialmente em dados maiores, mas geralmente foi mais lento que o QuickSort.

- **Selection Sort:** Muito mais lento que os outros algoritmos, especialmente em conjuntos de dados maiores. Não é adequado para grandes volumes de dados.

- **Algoritmo Híbrido (limite=16):** Teve desempenho próximo ao QuickSort em tamanhos menores, mas ficou atrás em conjuntos de dados maiores.

- **Algoritmo Híbrido (limite=64):** Mostrou um desempenho melhor em conjuntos de dados pequenos e médios, mas não foi significativamente melhor que o QuickSort.

- **Algoritmo Híbrido (limite=256):** Teve um desempenho similar ao limite de 64, com uma ligeira vantagem em tamanhos de dados muito grandes.
