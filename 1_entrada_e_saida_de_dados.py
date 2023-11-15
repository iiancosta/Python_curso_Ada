# LEIA A EXPLICAÇÃO NO ARQUIVO README.md

# Entrada de Dados input():
nome = input("Digite seu nome: ")
print("Olá,", nome)

# Saída de Dados print():
idade = 25
print("Sua idade é:", idade)

# Formatação de Saída:

# Usando % (Formatação Antiga):
nome = "João"
idade = 30
print("Nome: %s, Idade: %d" % (nome, idade))

# Usando format() (Método Recomendado):
nome = "Maria"
idade = 28
print("Nome: {}, Idade: {}".format(nome, idade))

# Usando f-Strings (Python 3.6+):
nome = "Pedro"
idade = 35
print(f"Nome: {nome}, Idade: {idade}")

# Leitura de Dados Numéricos:
numero = int(input("Digite um número inteiro: "))

'''
Manipulação de Arquivos:

Para entrada e saída de arquivos, você pode usar as funções `open()`, `read()`, `write()`, entre outras:

Leitura de um Arquivo:

with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

Escrita em um Arquivo:

with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Este é um exemplo de texto.")
'''