n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3

print(f"Menor = {menor}")

print("-"*50)

n1 = 0
n2 = 1
while n1 != n2:
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    if n1 < n2:
        print("Crescente")
    elif n2 < n1:
        print("Decrescente")
    else:
        print("Numeros iguais")

