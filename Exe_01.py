import math

base = float(input("Qual a base do retangulo: "))
altura = float(input("Qual a altura do retangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(math.pow(base, 2) + math.pow(altura, 2))

print(f"Area = {area:.2f}")
print(f"Perimetro = {perimetro:.2f}")
print(f"Diagonal = {diagonal:.2f}")

print("-"*50)

print("DADOS PRIMEIRA PESSOA:")
n1 = input("Nome: ")
id1 = int(input("Idade: "))
print("DADOS PRIMEIRA PESSOA:")
n2 = input("Nome: ")
id2 = int(input("Idade: "))

media = (id1 + id2) / 2

print(f"A idade média de {n1} e {n2} é de {media} anos!")

print("GABRIEL GOSTOSO")
print("GABRIEL LINDO")
print("GABRIEL GOSTOSO")