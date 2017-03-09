L = ['spam', 'Spam', 'SPAM!']

L[1] = 'eggs'     #altera L[1]

print(L)

L[0:2] = ['eat', 'more']      #substitui de 0:2

print(L)

L = ['abc', 'ABD', 'aBe']

L.sort(key=str.lower, reverse=True)   #ordena por ordem alfabetica, minusculas primeiro, e reverte a ordem

print(L)

print(sorted([x.lower() for x in L], reverse=True))  #passa para minisculas, ordena e reverte

L.extend([3,4,5])            #adiciona à lista

print(L)

L = ['spam', 'eggs', 'ham']

print(L.index('eggs'))     #index do objecto

L.insert(1,'toast')        #insere numa determinada posicao

print(L)

L.remove('eggs')       #remove por valor
L.pop(1)               #remove por index

print(L)

L = [1,2,3,4]

del L[1:]              #apaga um secçao inteira

print(L)

