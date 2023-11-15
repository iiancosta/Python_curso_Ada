# LEIA A EXPLICAÇÃO NO ARQUIVO README.md

# Declaração de Variáveis:

nome = "Alice"  # Aqui, 'nome' é uma variável do tipo string
idade = 25      # 'idade' é uma variável do tipo inteiro
pi = 3.14       # 'pi' é uma variável do tipo float
ativo = True    # 'ativo' é uma variável do tipo booleano


# Reatribuição de Variáveis:

idade = 30
idade = idade + 5  # Reatribuição - agora 'idade' é 35

# Variáveis como Referências:

a = [1, 2, 3]  # 'a' referencia uma lista
b = a          # 'b' agora referencia a mesma lista que 'a'
b.append(4)    # Isso modifica a lista referenciada por 'b'
print(a)       # Isso também afeta 'a', porque 'a' e 'b' referenciam o mesmo objeto na memória