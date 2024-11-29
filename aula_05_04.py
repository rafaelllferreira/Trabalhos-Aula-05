#
qtd_par = 0
qtd_impar = 0
numeros = [45,31,23,22,4,90,32,55,44,89]
num_sort = []
num_reverse = []

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        qtd_par += 1
    else:
        qtd_impar += 1

print(f"A quantidade de números pares é: {qtd_par}")
print(f"A quantidade de números ímpares é: {qtd_impar}")
print("Ordem de Criação:")
print(numeros)
print("Ordem Crescente:")
numeros.sort()
print(numeros)
print("Ordem Reversa:")
numeros.reverse()
print(numeros)
