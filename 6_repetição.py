# LEIA A EXPLICAÇÃO NO ARQUIVO README.md

# Estrutura de Repetição `for`:

# Exemplo com lista:
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)
# Saída:
# maçã
# banana
# laranja

for i in range(5):  # Gera números de 0 a 4
    print(i)
# Saída:
# 0
# 1
# 2
# 3
# 4

# Estrutura de Repetição `while`:
contador = 0
while contador < 5:
    print(contador)
    contador += 1
# Saída:
# 0
# 1
# 2
# 3
# 4


''' Comandos de Controle de Fluxo:
- break: Para a execução do loop antes que a condição se torne `False`.
- continue: Pula a iteração atual e continua para a próxima.
- else (pós-loop): Executa um bloco de código se o loop for concluído sem utilizar `break`.
'''

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop concluído sem interrupção.")
# Saída:
# 0
# 1
# 2

# Compreensão de Lista (List Comprehension):

numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numeros]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

#Exemplo com condicional:
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Saída: [0, 2, 4, 6, 8]