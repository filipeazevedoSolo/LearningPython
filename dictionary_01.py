D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}      #key:value

print(D)

D['name'] =  'bob'              #cria nova correspondencia

print(D)

L = {'name': {'first':'Bob','last':'Smith'},'job':['dev','mgr'],'age':40.5}

print(L['name'])            #vai buscar o valor da cheve

print(L['name']['last'])    #vai buscar o valor da chave last que faz parte do valor name

L['job'].append('janitor')  #adiciona mais um valor à lista de valores
print(L['job'])

D = {'a':1, 'b':2, 'c':3}

ks=list(D.keys())          #passa as chaves para uma lista
print(ks)

for key in sorted(D): print(key, '=>', D[key])   #percorre a lista ordenada(sorted) e imprime os valores de cada chave

