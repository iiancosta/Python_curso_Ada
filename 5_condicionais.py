# LEIA A EXPLICAÇÃO NO ARQUIVO README.md

# if:
idade = 20
if idade >= 18:
    print("Você é maior de idade.")

# if-else:
idade = 15
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# if-elif-else:
idade = 20
if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você acabou de atingir a maioridade.")
else:
    print("Você é maior de idade.")

'''
Operadores de Comparação:
- `==`: Igual a
- `!=`: Diferente de
- `>`: Maior que
- `<`: Menor que
- `>=`: Maior ou igual a
- `<=`: Menor ou igual a

Operadores Lógicos:
- `and`: Retorna `True` se ambas as condições forem verdadeiras.
- `or`: Retorna `True` se pelo menos uma das condições for verdadeira.
- `not`: Inverte o valor da condição.
'''

idade = 22
genero = "Masculino"

if idade >= 18 and genero == "Masculino":
    print("Você é um homem maior de idade.")