'''
# Como pedir dados no terminal usando input
nome = input("Nome:")
idade = int(input("IDade:"))
peso = float(input("Peso:"))

# Como saber qual tipo da variável usando type
print(nome)
print(idade, type(idade))
print(peso, type(peso))
'''
'''
# Operadores matemáticos
soma = 1 + 1
multiplicação = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print("Soma: ", soma)
print("Multiplicação: ", multiplicação)
print("Divisão: ", divisao)
print("Potência: ", potencia)
'''

# Condições 
'''
# Exemplo 1
idade = int(input("Informe idade: "))

if idade >= 18:
    print("Permitido")
else:
    print("Bloqueado") 


# Exemplo 2
salario = float(input("Informe o salário: "))

if salario > 0 and salario <= 3000:
    print("Programador Júnior")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador Sênior")
elif salario > 15000:
    print("Gerente de Projetos")
else:
    print("Valor deve ser positivo")
'''

'''
# Listas
# Exemplo 1
lista_numeros = [1,2,3]

lista_numeros[2] = 5

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

print("total de numeros": len(lista_numeros))
print("menor valor": min(lista_numeros))
print("maior valor": max(lista_numeros))
# Exemplo 2
lista_vazia = []

lista_vazia.append("Olá ")
lista_vazia.append("Mundo!")

print(lista_vazia)

# Comandos para listas
append = acrescenta um novo item no final da lista
insert = insere um novo item na posição dada
pop - sem posição = remove e retorna o ultimo item
pop - com posição = remove e retorno o item da posição
sort = ordena a lista
reverse = ordena a lista em ordem reversa
index = retorna a posição da primeira ocorrência do item
count = retorna o número de ocorrências do item
remove = remove a primeira ocorrência do item
'''

'''
# Repetições
notas = []

for x in range(5):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("Quantidade de notas: ", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM ", codigo_aluno, "tirou a nota: ", nota)


# Dicionários
# Exemplo 1
pessoa = {
    "nome": "Programador Python",
    "idade": 27,
    "peso": 70.2
}

print( pessoa['nome'])
print( pessoa['idade'])
print( pessoa['peso'])


# Exemplo 2
player = {
    "nome": "Guilherme",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano":5,
}

npcs = [
    {"nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    {"nome": "Monstro", "dano": 5, "hp": 100, "exp": 15},
    {"nome": "Monstrão", "dano": 10, "hp": 150, "exp": 25},
    {"nome": "Chefão", "dano": 25, "hp": 250, "exp": 35},
]


# Criando um chat com lista e dicionários
import os

mensagens = []
nome = input("Nome: ")

while True:
    os.system('cls')
    if len(mensagens)>0:
        for m in mensagens:
            print(m['nome'], " disse", "-", m['texto'])
    print("_______________________")

    texto = input("Mensagem: ")
    if texto == "fim":
        break

    mensagens.append({
        "nome": nome,
        "texto": texto
    })

'''

# Funções

def minha_funcao(valor1, valor2):
    
    return print ("Resultado: ", valor1 + valor2)

    

num1 = int(input("Valor1: "))
num2 = int(input("Valor2: "))

minha_funcao(num1, num2)


