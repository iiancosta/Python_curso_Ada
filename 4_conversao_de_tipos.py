# LEIA A EXPLICAÇÃO NO ARQUIVO README.md

''' Conversão de String para Número:

int(): Converte para inteiro.
float(): Converte para ponto flutuante. '''

numero_string = "10"
numero_inteiro = int(numero_string)
numero_float = float(numero_string)

print(numero_inteiro)  # Saída: 10
print(numero_float)    # Saída: 10.0

''' Conversão de Número para String: 

str(): Converte para string.'''

numero_inteiro = 10
numero_float = 3.14

numero_string_inteiro = str(numero_inteiro)
numero_string_float = str(numero_float)

print(numero_string_inteiro)  # Saída: "10"
print(numero_string_float)    # Saída: "3.14"

''' Conversão de String para Listas ou Tuplas:

split(): Divide uma string em substrings com base em um separador e retorna uma lista.
tuple(): Converte uma sequência (pode ser uma lista, string, etc.) em uma tupla. '''

frase = "Olá, mundo!"
lista_palavras = frase.split()  # Divide a frase em uma lista de palavras
tupla_palavras = tuple(lista_palavras)

print(lista_palavras)  # Saída: ['Olá,', 'mundo!']
print(tupla_palavras)  # Saída: ('Olá,', 'mundo!')

lista = [1, 2, 3]
tupla = tuple(lista)

print(tupla)  # Saída: (1, 2, 3)

''' Conversão de Tipos Lógicos:

bool(): Converte para booleano.'''

valor_inteiro = 0
valor_booleano = bool(valor_inteiro)

print(valor_booleano)  # Saída: False