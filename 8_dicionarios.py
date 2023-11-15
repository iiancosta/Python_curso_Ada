
# Criação de Dicionários:
dicionario_vazio = {}  # Dicionário vazio
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}  # Dicionário com dados

# Acesso a Elementos:
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
print(pessoas['Alice'])  # Saída: 25

'''
Adição, Remoção e Modificação de Elementos:
- Adição de Elementos: dicionario[chave] = valor.
- Remoção de Elementos: del dicionario[chave].
- Modificação de Elementos: Atribuição direta a uma chave existente.
'''
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
pessoas['David'] = 40  # Adiciona um novo elemento
del pessoas['Bob']  # Remove um elemento
pessoas['Alice'] = 26  # Modifica um valor existente

'''
Métodos Úteis para Dicionários:
- keys(): Retorna uma lista com as chaves do dicionário.
- values(): Retorna uma lista com os valores do dicionário.
- items(): Retorna uma lista de tuplas (chave, valor).
- get(): Retorna o valor associado a uma chave, ou um valor padrão se a chave não existir.
- update(): Atualiza o dicionário com outro dicionário ou pares de chave-valor.
'''
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
chaves = pessoas.keys()
valores = pessoas.values()
itens = pessoas.items()
valor = pessoas.get('Alice')
pessoas.update({'Alice': 26, 'David': 40})

# Verificação de Existência de Chaves:
#- in: Verifica se uma chave existe no dicionário.

pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
existe_bob = 'Bob' in pessoas  # Retorna True
existe_emily = 'Emily' in pessoas  # Retorna False

'''
Iteração em Dicionários:
- Iteração por Chaves: for chave in dicionario:.
- teração por Valores: for valor in dicionario.values().
- Iteração por Chave-Valor: for chave, valor in dicionario.items().
'''

pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
for chave in pessoas:
    print(chave)  # Imprime as chaves
for valor in pessoas.values():
    print(valor)  # Imprime os valores
for chave, valor in pessoas.items():
    print(chave, valor)  # Imprime chave e valor