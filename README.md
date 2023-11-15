# Python_curso_Ada
Nesse documento apresento meus aprendizados no módulo de Pyhton da trilha digital da Ada Tech.

## índice
1. [Entrada e saída de dados](#entrada)
2. [Variáveis](#variaveis)
3. [Operadores aritméticos e boleanos](#operadores)
4. [Conversão de tipos](#conversão)
5. [Estruturas condicionais](#condicionais)
6. [Estruturas de repetição](#repetição)
7. [Lista](#listas)
8. [Dicionários](#dicionários)
9. [Funções](#funções)
10. [Lambda](#lambda)<div id='entrada'/>

## **Entrada e saída de dados**

Em Python, a entrada e saída de dados são realizadas principalmente por meio das funções `input()` e `print()`.

### Entrada de Dados (`input()`):
A função `input()` permite que o usuário insira dados a partir do teclado. Ela recebe uma mensagem opcional para exibir antes de esperar pela entrada do usuário. Por exemplo:

```python
nome = input("Digite seu nome: ")
print("Olá,", nome)
```

### Saída de Dados (`print()`):
A função `print()` é usada para exibir dados na tela. Ela pode receber vários argumentos e imprimir variáveis junto com texto formatado. Por exemplo:

```python
idade = 25
print("Sua idade é:", idade)
```

### Formatação de Saída:
A formatação pode ser feita usando métodos diferentes:

#### Usando `%` (Formatação Antiga):
```python
nome = "João"
idade = 30
print("Nome: %s, Idade: %d" % (nome, idade))
```

#### Usando `format()` (Método Recomendado):
```python
nome = "Maria"
idade = 28
print("Nome: {}, Idade: {}".format(nome, idade))
```

#### Usando f-Strings (Python 3.6+):
```python
nome = "Pedro"
idade = 35
print(f"Nome: {nome}, Idade: {idade}")
```

### Leitura de Dados Numéricos:
Por padrão, `input()` retorna uma string. Se você deseja receber um número inteiro ou flutuante, pode convertê-lo explicitamente usando `int()` ou `float()`:

```python
numero = int(input("Digite um número inteiro: "))
```

### Manipulação de Arquivos:
Para entrada e saída de arquivos, você pode usar as funções `open()`, `read()`, `write()`, entre outras:

#### Leitura de um Arquivo:
```python
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

#### Escrita em um Arquivo:
```python
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Este é um exemplo de texto.")
```

Esses são métodos comuns para entrada e saída de dados em Python, permitindo interações com o usuário, formatação de saída e manipulação de arquivos. <div id='variaveis'/>
 
## **Variáveis Pyhton**

Em Python, as variáveis são usadas para armazenar dados. Elas são criadas quando você atribui um valor a elas pela primeira vez. Aqui estão algumas características importantes sobre variáveis em Python:

### Declaração de Variáveis:
Você não precisa declarar explicitamente o tipo de uma variável em Python. Atribuir um valor a uma variável cria-a e determina automaticamente o tipo com base no valor atribuído.

Exemplo:
```python
nome = "Alice"  # Aqui, 'nome' é uma variável do tipo string
idade = 25      # 'idade' é uma variável do tipo inteiro
pi = 3.14       # 'pi' é uma variável do tipo float
ativo = True    # 'ativo' é uma variável do tipo booleano
```

### Nomes de Variáveis:
- Devem começar com uma letra (a-z, A-Z) ou um sublinhado (_).
- Podem conter letras, números e sublinhados.
- São sensíveis a maiúsculas e minúsculas (`Nome` é diferente de `nome`).

### Convenções de Nomenclatura:
- Use nomes descritivos para suas variáveis para facilitar a compreensão do código.
- Use nomes em minúsculas para variáveis com várias palavras separadas por sublinhados para aumentar a legibilidade (ex: `nome_completo`, `idade_usuario`).

### Reatribuição de Variáveis:
Você pode reatribuir um valor a uma variável quantas vezes quiser, independentemente do tipo de dado inicial.

Exemplo:
```python
idade = 30
idade = idade + 5  # Reatribuição - agora 'idade' é 35
```

### Tipagem Dinâmica:
Python é uma linguagem de tipagem dinâmica, o que significa que você não precisa definir o tipo de variável explicitamente. O tipo é inferido com base no valor atribuído.

### Variáveis como Referências:
Em Python, as variáveis são referências a objetos na memória. Quando você faz uma atribuição, está associando o nome da variável a um objeto específico na memória.

Exemplo:
```python
a = [1, 2, 3]  # 'a' referencia uma lista
b = a          # 'b' agora referencia a mesma lista que 'a'
b.append(4)    # Isso modifica a lista referenciada por 'b'
print(a)       # Isso também afeta 'a', porque 'a' e 'b' referenciam o mesmo objeto na memória
```

Variáveis em Python são fundamentais para armazenar e manipular dados, e a compreensão do seu comportamento ajuda na escrita de códigos eficientes e funcionais. <div id='operadores'/>


## **Operadores aritméticos e boleanos**

Os operadores aritméticos e booleanos são fundamentais em Python para realizar cálculos matemáticos e operações lógicas. Aqui estão os principais:

### Operadores Aritméticos:
- `+`: Adição
- `-`: Subtração
- `*`: Multiplicação
- `/`: Divisão
- `//`: Divisão inteira (retorna apenas a parte inteira da divisão)
- `%`: Módulo (retorna o resto da divisão)
- `**`: Exponenciação

Exemplo de uso:
```python
a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto_divisao = a % b
exponenciacao = a ** b
```

### Operadores Booleanos:
- `and`: Retorna True se ambos os operandos forem True, caso contrário, retorna False.
- `or`: Retorna True se pelo menos um dos operandos for True, caso contrário, retorna False.
- `not`: Retorna o oposto do valor booleano do operando.

Exemplo de uso:
```python
x = True
y = False

resultado_and = x and y
resultado_or = x or y
resultado_not = not x
```

### Comparadores:
- `==`: Igual a
- `!=`: Diferente de
- `>`: Maior que
- `<`: Menor que
- `>=`: Maior ou igual a
- `<=`: Menor ou igual a

Exemplo de uso:
```python
a = 10
b = 5

igual = a == b
diferente = a != b
maior = a > b
menor = a < b
maior_igual = a >= b
menor_igual = a <= b
```

Estes operadores são essenciais para realizar operações matemáticas, lógicas e comparações em Python, permitindo que você crie lógica condicional, iterações e muito mais. <div id='conversão'/>

## **Conversão de tipos**

Em Python, é possível converter entre diferentes tipos de dados usando funções específicas para cada tipo de conversão. Aqui estão algumas das conversões mais comuns:

### Conversão de String para Número:
- `int()`: Converte para inteiro.
- `float()`: Converte para ponto flutuante.

Exemplo:
```python
numero_string = "10"
numero_inteiro = int(numero_string)
numero_float = float(numero_string)

print(numero_inteiro)  # Saída: 10
print(numero_float)    # Saída: 10.0
```

### Conversão de Número para String:
- `str()`: Converte para string.

Exemplo:
```python
numero_inteiro = 10
numero_float = 3.14

numero_string_inteiro = str(numero_inteiro)
numero_string_float = str(numero_float)

print(numero_string_inteiro)  # Saída: "10"
print(numero_string_float)    # Saída: "3.14"
```

### Conversão de String para Listas ou Tuplas:
- `split()`: Divide uma string em substrings com base em um separador e retorna uma lista.
- `tuple()`: Converte uma sequência (pode ser uma lista, string, etc.) em uma tupla.

Exemplo:
```python
frase = "Olá, mundo!"
lista_palavras = frase.split()  # Divide a frase em uma lista de palavras
tupla_palavras = tuple(lista_palavras)

print(lista_palavras)  # Saída: ['Olá,', 'mundo!']
print(tupla_palavras)  # Saída: ('Olá,', 'mundo!')

lista = [1, 2, 3]
tupla = tuple(lista)

print(tupla)  # Saída: (1, 2, 3)
```

### Conversão de Tipos Lógicos:
- `bool()`: Converte para booleano.

Exemplo:
```python
valor_inteiro = 0
valor_booleano = bool(valor_inteiro)

print(valor_booleano)  # Saída: False
```

Estas funções ajudam a converter entre diferentes tipos de dados em Python, permitindo a flexibilidade no tratamento de dados em um programa. <div id='condicionais'/>

## **Estruturas condicionais**

As estruturas condicionais em Python permitem que você tome decisões com base em condições. As principais estruturas são o `if`, `elif` (abreviação de "else if") e `else`. Veja como elas funcionam:

### if:
O `if` é usado para executar um bloco de código se uma condição for verdadeira.

```python
idade = 20

if idade >= 18:
    print("Você é maior de idade.")
```

### if-else:
O `else` é usado para executar um bloco de código caso a condição do `if` não seja verdadeira.

```python
idade = 15

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

### if-elif-else:
O `elif` é usado para verificar múltiplas condições. Se a condição de um `if` ou `elif` for verdadeira, o restante das condições não será verificado.

```python
idade = 20

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você acabou de atingir a maioridade.")
else:
    print("Você é maior de idade.")
```

### Operadores de Comparação:
- `==`: Igual a
- `!=`: Diferente de
- `>`: Maior que
- `<`: Menor que
- `>=`: Maior ou igual a
- `<=`: Menor ou igual a

### Operadores Lógicos:
- `and`: Retorna `True` se ambas as condições forem verdadeiras.
- `or`: Retorna `True` se pelo menos uma das condições for verdadeira.
- `not`: Inverte o valor da condição.

Exemplo com operadores lógicos:
```python
idade = 22
genero = "Masculino"

if idade >= 18 and genero == "Masculino":
    print("Você é um homem maior de idade.")
```

As estruturas condicionais em Python são essenciais para controlar o fluxo do seu programa e tomar decisões com base em diferentes condições. <div id='repetição'/>

## **Estruturas de repetição**

Em Python, existem duas principais estruturas de repetição: `for` e `while`. Elas permitem executar um bloco de código várias vezes, mas com diferentes abordagens.

### Estrutura de Repetição `for`:
O `for` é usado para iterar sobre uma sequência (lista, tupla, dicionário, etc.) ou um iterável. Ele executa um bloco de código para cada item na sequência.

Exemplo com lista:
```python
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)
# Saída:
# maçã
# banana
# laranja
```

O `for` também pode ser usado com a função `range()` para gerar uma sequência numérica.

Exemplo com `range()`:
```python
for i in range(5):  # Gera números de 0 a 4
    print(i)
# Saída:
# 0
# 1
# 2
# 3
# 4
```

### Estrutura de Repetição `while`:
O `while` é usado quando você deseja repetir um bloco de código enquanto uma condição for verdadeira.

Exemplo:
```python
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
```

**Atenção**: Com o `while`, é essencial garantir que a condição seja eventualmente `False`, ou você pode entrar em um loop infinito.

### Comandos de Controle de Fluxo:
- `break`: Para a execução do loop antes que a condição se torne `False`.
- `continue`: Pula a iteração atual e continua para a próxima.
- `else` (pós-loop): Executa um bloco de código se o loop for concluído sem utilizar `break`.

Exemplo com `break` e `else`:
```python
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
```

As estruturas de repetição `for` e `while` são fundamentais em Python para iterar sobre dados, realizar tarefas repetitivas e controlar o fluxo de execução do programa.

Além do `for` e `while`, o Python oferece uma estrutura adicional que é menos comum, mas pode ser poderosa em determinados contextos: a compreensão de lista (`list comprehension`). 

### Compreensão de Lista (List Comprehension):

A compreensão de lista é uma maneira concisa e eficiente de criar listas em Python. Ela permite criar uma lista baseada em alguma expressão ou condição aplicada a cada item de um iterável.

Exemplo simples:
```python
numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numeros]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
```

Também é possível aplicar condicionais dentro da compreensão de lista:

Exemplo com condicional:
```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Saída: [0, 2, 4, 6, 8]
```

A compreensão de lista oferece uma maneira elegante e compacta de criar listas aplicando transformações ou filtragens em uma única linha de código.

Além dessas estruturas, as iterações em Python são frequentemente realizadas usando bibliotecas como `numpy` ou `pandas`, que oferecem funcionalidades avançadas para lidar com dados em arrays multidimensionais ou para análise de dados, mas essas não são estruturas de repetição por si só, são bibliotecas que oferecem métodos específicos para iterar e manipular dados. <div id='listas'/>

## **Listas**

As listas em Python são uma estrutura de dados fundamental, flexível e muito utilizada. Aqui está uma cobertura detalhada sobre listas:

### O que são Listas?
- **Coleção ordenada**: Armazena elementos em uma sequência ordenada e mutável.
- **Heterogêneas**: Podem conter diferentes tipos de dados (números, strings, listas, etc.).
- **Mutáveis**: É possível alterar, adicionar e remover elementos.

### Criação de Listas:
```python
lista_vazia = []  # Lista vazia
numeros = [1, 2, 3, 4, 5]  # Lista de números
misturada = [1, 'dois', True, 3.14]  # Lista com diferentes tipos de dados
```

### Acesso a Elementos:
- Os elementos são acessados por índices (começando do 0).
```python
numeros = [1, 2, 3, 4, 5]
print(numeros[0])  # Saída: 1
print(numeros[-1])  # Último elemento, saída: 5
```

### Modificação de Listas:
- **Adição de elementos**: `append()`, `extend()`, `insert()`.
- **Remoção de elementos**: `pop()`, `remove()`, `del`.
- **Alteração de elementos**: Modificando diretamente pelo índice.
```python
lista = [1, 2, 3]
lista.append(4)  # Adiciona um elemento ao final
lista.extend([5, 6])  # Adiciona elementos de outra lista ao final
lista.insert(1, 'dois')  # Insere 'dois' no índice 1
lista.pop()  # Remove o último elemento e retorna-o
lista.remove('dois')  # Remove o elemento 'dois'
del lista[0]  # Remove o elemento no índice 0
```

### Operações com Listas:
- **Concatenação**: `+`
- **Repetição**: `*`
```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2  # Concatenação
repetida = lista1 * 3  # Repetição
```

### Métodos e Funções Úteis para Listas:
- `len()`: Retorna o tamanho da lista.
- `index()`: Retorna o índice do primeiro item encontrado.
- `count()`: Conta o número de ocorrências de um elemento.
- `sort()`: Ordena a lista.
- `reverse()`: Inverte a ordem dos elementos.
- `max()`: apresenta o maior valor da lista.
- `min()`: apresenta o menor valor da lista.
- `sum()`: soma os valores da lista.
```python
lista = [3, 1, 2, 3]
tamanho = len(lista)
indice = lista.index(2)
ocorrencias = lista.count(3)
lista.sort()
lista.reverse()
maior = max(lista)
menor = min(lista)
soma = sum(lista)
```

As listas são muito versáteis e uma das estruturas de dados mais utilizadas em Python devido à sua flexibilidade e facilidade de uso. Elas são amplamente empregadas em iterações, armazenamento de dados e manipulação de informações em geral. <div id='dicionários'/>

## **Dicionários**

Os dicionários em Python são estruturas de dados poderosas que permitem armazenar pares de chave-valor. Aqui está uma cobertura completa sobre dicionários:

### O que são Dicionários?
- **Coleção mutável**: Permite armazenar pares de chave-valor.
- **Sem ordem definida**: Os elementos não são acessados por índices, mas sim por suas chaves únicas.
- **Chaves únicas**: Cada chave em um dicionário é única.

### Criação de Dicionários:
```python
dicionario_vazio = {}  # Dicionário vazio
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}  # Dicionário com dados
```

### Acesso a Elementos:
- Os elementos são acessados pela chave.
```python
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
print(pessoas['Alice'])  # Saída: 25
```

### Adição, Remoção e Modificação de Elementos:
- **Adição de Elementos**: `dicionario[chave] = valor`.
- **Remoção de Elementos**: `del dicionario[chave]`.
- **Modificação de Elementos**: Atribuição direta a uma chave existente.
```python
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
pessoas['David'] = 40  # Adiciona um novo elemento
del pessoas['Bob']  # Remove um elemento
pessoas['Alice'] = 26  # Modifica um valor existente
```

### Métodos Úteis para Dicionários:
- `keys()`: Retorna uma lista com as chaves do dicionário.
- `values()`: Retorna uma lista com os valores do dicionário.
- `items()`: Retorna uma lista de tuplas (chave, valor).
- `get()`: Retorna o valor associado a uma chave, ou um valor padrão se a chave não existir.
- `update()`: Atualiza o dicionário com outro dicionário ou pares de chave-valor.
```python
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
chaves = pessoas.keys()
valores = pessoas.values()
itens = pessoas.items()
valor = pessoas.get('Alice')
pessoas.update({'Alice': 26, 'David': 40})
```

### Verificação de Existência de Chaves:
- `in`: Verifica se uma chave existe no dicionário.
```python
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
existe_bob = 'Bob' in pessoas  # Retorna True
existe_emily = 'Emily' in pessoas  # Retorna False
```

### Iteração em Dicionários:
- **Iteração por Chaves**: `for chave in dicionario:`.
- **Iteração por Valores**: `for valor in dicionario.values()`.
- **Iteração por Chave-Valor**: `for chave, valor in dicionario.items()`.
```python
pessoas = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
for chave in pessoas:
    print(chave)  # Imprime as chaves
for valor in pessoas.values():
    print(valor)  # Imprime os valores
for chave, valor in pessoas.items():
    print(chave, valor)  # Imprime chave e valor
```

Os dicionários são uma estrutura de dados versátil em Python, permitindo armazenar e manipular dados de forma eficiente, associando valores a chaves únicas para uma rápida recuperação de informações. <div id='funções'/>

## **Funções**

Em Python, as funções são blocos de código reutilizáveis que realizam uma tarefa específica quando chamadas. Elas são fundamentais para organizar e modularizar o código. Aqui estão os elementos essenciais sobre funções em Python:

### Sintaxe Básica:
```python
def nome_da_funcao(parametros):
    # Corpo da função
    # Pode conter uma ou mais instruções
    return resultado  # Opcional: pode retornar um valor
```

- `def`: Palavra-chave usada para definir uma função.
- `nome_da_funcao`: Identificador da função.
- `parâmetros`: Valores que a função aceita (opcionais).
- `return`: Palavra-chave usada para retornar um valor (opcional).

### Exemplo Simples de Função:
```python
def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("Alice")
print(mensagem)  # Saída: "Olá, Alice!"
```

### Parâmetros de Função:
- **Parâmetros Posicionais**: Passados na mesma ordem em que foram definidos.
- **Parâmetros Nomeados (Keyword Arguments)**: Identificados pelo nome do parâmetro.
- **Valores Padrão**: Parâmetros com valores predefinidos.

Exemplo:
```python
def boas_vindas(nome, mensagem="Bem-vindo"):
    return f"{mensagem}, {nome}!"

msg1 = boas_vindas("Alice")  # Usando o valor padrão
msg2 = boas_vindas("Bob", "Olá")  # Passando mensagem explicitamente
msg3 = boas_vindas(mensagem="Oi", nome="Charlie")  # Passando parâmetros nomeados
```

### Escopo de Variáveis:
- **Variáveis Locais**: Definidas dentro da função e acessíveis apenas lá.
- **Variáveis Globais**: Definidas fora da função e acessíveis em qualquer lugar do código.

### Funções Aninhadas:
- Definição de funções dentro de outras funções.
- Úteis para dividir problemas complexos em partes menores.

Claro, as funções em Python são blocos de código que realizam uma tarefa específica e podem ser reutilizadas em diferentes partes do programa. Aqui estão mais detalhes sobre funções:

### Parâmetros Arbitrários:
- `*args`: Recebe um número arbitrário de argumentos posicionais como uma tupla.
- `**kwargs`: Recebe um número arbitrário de argumentos nomeados como um dicionário.

Exemplo:
```python
def soma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

total = soma(1, 2, 3, 4, 5)  # Pode receber qualquer número de argumentos
```

### Retorno de Múltiplos Valores:
Uma função pode retornar múltiplos valores empacotados em uma tupla.

Exemplo:
```python
def opera_numeros(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

resultado = opera_numeros(8, 3)
print(resultado)  # Saída: (11, 5)
```

### Documentação de Funções (Docstrings):
- Strings de documentação que explicam o propósito e comportamento da função.
- Acessadas usando `help()` ou `__doc__`.

Exemplo:
```python
def calcular_area(base, altura):
    """Calcula a área de um retângulo."""
    return base * altura

print(help(calcular_area))  # Exibe a documentação da função
```

### Funções como Objetos:
- Em Python, as funções são tratadas como objetos, o que significa que podem ser atribuídas a variáveis, passadas como argumentos ou retornadas por outras funções.

Exemplo:
```python
def saudacao(nome):
    return f"Olá, {nome}!"

outra_saudacao = saudacao  # Atribuindo a função a outra variável
print(outra_saudacao("Alice"))  # Saída: "Olá, Alice!"
```

### Recursividade:
- Uma função que chama a si mesma.
- Útil para resolver problemas que podem ser divididos em casos menores.

Exemplo (Fatorial):
```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))  # Saída: 120
```

As funções em Python oferecem flexibilidade e facilitam a criação de código modular e organizado. Com diferentes recursos e técnicas, é possível criar funções poderosas para diversas necessidades de programação. <div id='lambda'/>

## LAMBDA

O `lambda` em Python é uma expressão que cria funções anônimas, ou seja, funções pequenas e sem nome. Eles são úteis para criar funções simples e rápidas sem a necessidade de definir uma função formal usando `def`.

A estrutura geral de um `lambda` é: `lambda argumentos: expressao`.

### Características do `lambda`:
- **Anonimato**: Não tem um nome associado, ao contrário das funções definidas por `def`.
- **Expressões Únicas**: Consiste apenas em uma única expressão, cujo resultado é retornado automaticamente.

### Utilização do `lambda`:
- **Funções de Única Linha**: São ideais para funções de única linha que realizam operações simples.
- **Passagem de Funções**: Úteis ao passar funções como argumentos para outras funções (`map()`, `filter()`, etc.).

Exemplo:
```python
dobrar = lambda x: x * 2
print(dobrar(5))  # Saída: 10
```

### Aplicações com `lambda`:
- **`map()`**: Aplica uma função a cada item de um iterável.
```python
numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x ** 2, numeros)
print(list(quadrados))  # Saída: [1, 4, 9, 16, 25]
```

- **`filter()`**: Filtra os elementos de um iterável com base em uma função.
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Saída: [2, 4, 6, 8, 10]
```

- **Ordenação Personalizada com `sorted()`**: Especifica uma função de chave para classificar itens.
```python
palavras = ['banana', 'maçã', 'abacaxi', 'laranja']
ordenadas = sorted(palavras, key=lambda x: len(x))
print(ordenadas)  # Saída: ['maçã', 'banana', 'laranja', 'abacaxi']
```

O `lambda` é poderoso, mas deve ser usado com moderação, priorizando a legibilidade do código. Em situações mais complexas, é preferível utilizar `def` para funções mais elaboradas.