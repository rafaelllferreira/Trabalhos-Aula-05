# Programa que mostra o uso de Listas
nomes_01 = "Alessandro, Maria, Eduarda"
nomes_02 = ["Alessandro", "Maria", "Eduarda"]
print(nomes_01)
print(nomes_02)
print(nomes_02[1])
print(len(nomes_02))
print("Listagem dos elementos do vetor:")
n = 1
for i in range (len(nomes_02)):
    print(f"{n}º - {nomes_02[i]}")
    n += 1
