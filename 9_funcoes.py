# LEIA A EXPLICAÇÃO NO ARQUIVO README.md

'''
- def: Palavra-chave usada para definir uma função.
- nome_da_funcao: Identificador da função.
- parâmetros: Valores que a função aceita (opcionais).
- return: Palavra-chave usada para retornar um valor (opcional).
'''

# Sintaxe Básica:
def nome_da_funcao(parametros):
    # Corpo da função
    # Pode conter uma ou mais instruções
    return resultado  # Opcional: pode retornar um valor

# Exemplo Simples de Função:
def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("Alice")
print(mensagem)  # Saída: "Olá, Alice!"

'''
Parâmetros de Função:
- Parâmetros Posicionais: Passados na mesma ordem em que foram definidos.
- Parâmetros Nomeados (Keyword Arguments): Identificados pelo nome do parâmetro.
- Valores Padrão: Parâmetros com valores predefinidos.
'''
def boas_vindas(nome, mensagem="Bem-vindo"):
    return f"{mensagem}, {nome}!"

msg1 = boas_vindas("Alice")  # Usando o valor padrão
msg2 = boas_vindas("Bob", "Olá")  # Passando mensagem explicitamente
msg3 = boas_vindas(mensagem="Oi", nome="Charlie")  # Passando parâmetros nomeados

'''
Parâmetros Arbitrários:
- args: Recebe um número arbitrário de argumentos posicionais como uma tupla.
- kwargs: Recebe um número arbitrário de argumentos nomeados como um dicionário.
'''

def soma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

total = soma(1, 2, 3, 4, 5)  # Pode receber qualquer número de argumentos


### Retorno de Múltiplos Valores:
def opera_numeros(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

resultado = opera_numeros(8, 3)
print(resultado)  # Saída: (11, 5)


'''
 Documentação de Funções (Docstrings):
- Strings de documentação que explicam o propósito e comportamento da função.
- Acessadas usando help() ou __doc__.
'''
def calcular_area(base, altura):
    """Calcula a área de um retângulo."""
    return base * altura

print(help(calcular_area))  # Exibe a documentação da função


# Funções como Objetos:
def saudacao(nome):
    return f"Olá, {nome}!"

outra_saudacao = saudacao  # Atribuindo a função a outra variável
print(outra_saudacao("Alice"))  # Saída: "Olá, Alice!"

'''
 Recursividade:
- Uma função que chama a si mesma.
- Útil para resolver problemas que podem ser divididos em casos menores.
'''
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))  # Saída: 120