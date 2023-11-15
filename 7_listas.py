# LEIA A EXPLICAÇÃO NO ARQUIVO README.md

# Criação de Listas:

lista_vazia = []  # Lista vazia
numeros = [1, 2, 3, 4, 5]  # Lista de números
misturada = [1, 'dois', True, 3.14]  # Lista com diferentes tipos de dados

# Acesso a Elementos:
numeros = [1, 2, 3, 4, 5]
print(numeros[0])  # Saída: 1
print(numeros[-1])  # Último elemento, saída: 5

''' Modificação de Listas:
- Adição de elementos: append(), extend(), insert().
- Remoção de elementos: Pop(), remove(), del.
- Alteração de elementos: Modificando diretamente pelo índice.
'''
lista = [1, 2, 3]
lista.append(4)  # Adiciona um elemento ao final
lista.extend([5, 6])  # Adiciona elementos de outra lista ao final
lista.insert(1, 'dois')  # Insere 'dois' no índice 1
lista.pop()  # Remove o último elemento e retorna-o
lista.remove('dois')  # Remove o elemento 'dois'
del lista[0]  # Remove o elemento no índice 0

'''
Operações com Listas:
- Concatenação: +
- Repetição: *
'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2  # Concatenação
repetida = lista1 * 3  # Repetição


'''
Métodos e Funções Úteis para Listas:
- len(): Retorna o tamanho da lista.
- index(): Retorna o índice do primeiro item encontrado.
- count(): Conta o número de ocorrências de um elemento.
- sort(): Ordena a lista.
- reverse(): Inverte a ordem dos elementos.
- max(): apresenta o maior valor da lista.
- min(): apresenta o menor valor da lista.
- sum(): soma os valores da lista.
'''
lista = [3, 1, 2, 3]
tamanho = len(lista)
indice = lista.index(2)
ocorrencias = lista.count(3)
lista.sort()
lista.reverse()
maior = max(lista)
menor = min(lista)
soma = sum(lista)