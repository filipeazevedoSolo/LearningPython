d = dict([('name','mel'), ('age',45)])

print(d)

L = ['a','b','c']

T = [1,2,3]

D = dict(zip(L,T))

print(D)

K = D.keys()
X = D.values()

print(K)
print(X)

del D['b']

print(K)          #apagando em D, altera K e X
print(X)

for k in sorted(D) : print(k,D[k])   #imprimir com sort nas chaves