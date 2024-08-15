
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

if n1 > n2:
    troca = n1
    n1 = n2
    n2 = troca

soma = 0
while n1 < n2:
    if n1 % 2 != 0:
        soma += n1
    n1+=1

print(f"Soma dos impares: {soma}")

print("-"*50)

lista = []

quant = int(input("Qunatos numeros adicionar: "))

cont = 0
soma1 = 0
while cont < quant:
    lista.append(int(input("Digite um numero: ")))
    soma1 += lista[cont]
    cont += 1

media = soma1 / quant

print("LISTA GERADA = ", end="")
cont = 0
while cont < quant:
    print(lista[cont], end=" ")
    cont += 1

print()
print(f"Soma = {soma1}")
print(f"Media = {media}")

print("-"*50)

ordem = int(input("Qual a ordem da matriz: "))

mat: [int] = []

conti = 0
while conti < ordem:
    contj = 0
    mat.append([])
    while contj < ordem:
        mat[conti].append(int(input(f"Elemento[{conti},{contj}]: ")))
        contj = contj + 1
    conti = conti + 1

print("Diagonal principal:")
conti = 0

while conti < ordem:
    print(mat[conti][conti], end=" ")
    conti += 1

