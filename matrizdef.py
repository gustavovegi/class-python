def printa_elemento (matriz):
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            print(f"matriz [{i}][{j}]")
    return

def mostra_matriz(matriz):
    for i in range (len(matriz)):
        print(matriz[i])
    return

coluna = 4
linha = 3
linhas= 3
def cria_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        matriz.append([])
        print(matriz)
        for j in range (coluna):
            matriz[i].append(0)
    return matriz


matriz1 = cria_matriz(10,10)
for i in range (len(matriz1)):
    for j in range (len(matriz1[0])):
        if i%2==0:
            matriz1[i][j]=1
mostra_matriz(matriz1)