def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz

def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma+=elem
    return soma
'''
matriz1 = cria_matriz(5, 1)
matriz2= cria_matriz(5, 1)

print(soma_defs(matriz))
'''
pesos = [1, 2, 3, 2, 1]
notas = cria_matriz(5,10)
medias = []
for i in range(len(pesos)):
    for j in range(notas[0]):
      soma += pesos[i]* notas[i][j]

media

mostra_matriz(notas)
print(soma)


#professor way
def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma+=elem
    return soma

alunos = 10
pesos = [1, 2, 3, 2, 1]
notas = cria_matriz(5,alunos)
medias = []

soma_pesos = soma_lista(pesos)
mostra_matriz(notas)

for j in range(alunos):
    soma = 0
    for i in range(len(pesos)):
        soma += pesos[i] * notas[i][j]
    media = soma/soma_pesos
    medias.append(media)
print(medias)