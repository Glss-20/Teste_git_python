
print('DEUS É BOM')

print("-"*50)

idade: int
salario: float
altura: float
genero: str
nome: str

idade = 20
salario = 5800
altura = 1.63
genero = "M"
nome = "Marcelo"

print(f"Idade = {idade}")
print(f"Salario = {salario:.2f}")
print(f"Altura = {altura}")
print(f"Genero = {genero}")
print(f"Nome = {nome}")

print("-"*50)

print("Bom dia!", end="") #O "end=" faz com que a linha não seja quebrada
print("Boa noite!")

print("-"*50)
print("ENTRADA DE DADOS")

s1 = float(input("Salário primeira pessoa: "))
n1 = input("Nome primeira pessoa: ")

s2 = float(input("Salario segunda pessoa: "))
n2 = input("Nome segunda pessoa: ")

id = input("Diga uma idade: ")
sx = input("Diga um sexo: ")

print(f"Nome 1 = {n1}")
print(f"Salario 1 = {s1:.2f}")
print(f"Nome 2 = {n2}")
print(f"Salario 2 = {s2:.2f}")
print(f"Idade = {id}")
print(f"Sexo = {sx}")

print("-"*50)
print("CONDICIONAL")

hora = 10

if hora < 12:
    print("Bom dia!")
elif hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")

print("-"*50)
print("ENQUANTO")

soma = 0
num = 1
while num != 0:
    num = int(input("Digite um número: "))
    soma = soma + num

print(f"SOMA = {soma}")

print("-"*50)
print("VET0R")

lista = []

quant = int(input("Quantos numeros adicionar: "))

cont = 0
while cont < quant:
    lista.append(int(input("Digite um numero: ")))
    cont = cont + 1

cont = 0
print("VALORES DIGITADOS:")
while cont < quant:
    print(lista[cont])
    cont = cont + 1

print("-"*50)
print("MATRIZ")

l = int(input("Quantas linhas tem a matriz: "))
c = int(input("Quantas colunas tem a matriz: "))

mat: [int] = []

conti = 0
while conti < l:
    contj = 0
    mat.append([])
    while contj < c:
        mat[conti].append(int(input(f"Elemento[{conti},{contj}]: ")))
        contj = contj + 1
    conti = conti + 1

print("MATRIZ GERADA")
conti = 0
while conti < l:
    contj = 0
    while contj < c:
        print(mat[conti][contj], end=" ")
        contj = contj + 1
    print()
    conti = conti + 1

print("GABRIEL LINDO")
print("GABRIEL GOSTOSO")

print("GABRIEL MARAVILHOSO")
print("GABRIEL BELO")
