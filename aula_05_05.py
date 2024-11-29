#Programa para quantidade de acertos de um gabarito!
gabarito = ["a","b","b","d","e"]
resp = []
acertos = 0
erros = 0

for i in range(5):
    resp.append(input("Informe a resposta: "))
    if gabarito [i] == resp[i]:
        acertos += 1
    else:
     erros += 1

print(f" Quantidade de respostas corretas: {acertos}")
print(f" Quantidade de respostas erradas: {erros}")

