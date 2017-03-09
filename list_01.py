L = [123, 'spam', 1.23]

L.append('NI')   #adiciona objeto ao fim da lista

print(L)

L.pop(3)     #remove objeto na posicao indicada

print(L)

del L[1]
del L[1]

L.append(10)
L.append(25)

print(L) 

L.sort()      #ordena lista (impossivel ordenar strings com ints)

print(L)

L.reverse()    #reverte a lista

print(L)

M = [[1,2,3],[4,4,8],[5,2,0]]    #matriz

col3 = [row[2] for row in M]  #todos os valores da 3 coluna

print(col3)

F = [row[0] for row in M if row[0] % 2 == 0]   #numeros pares da coluna 0

print(F)


diag = [M[i][i] for i in [2,1,0]]     #diagonal matriz

print(diag)


G = (sum(row) for row in M)         #gerador de somas de linhas

print(next(G))


G = list(map(sum, M))             #lista com soma de todas as linhas

print(G)


