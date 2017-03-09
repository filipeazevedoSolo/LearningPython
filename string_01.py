S = 'Aada'
print(len(S)) #tamanho

print(S[1:]) #tudo desde 1

S = 'z' + S[1:3] #altera S para z + tudo desde 1 ate 3(n incluido)

print(S)

S.find('a')     #encontra 'a' na string

S = S.replace('a','y')   #troca todos os 'a' por 'y'

print(S)

l = 'ad,c'

l.split(',')   #divide por ','

l.upper()      #maiusculas

print('{0}, eggs, and {1}'.format('spam', 'SPAM'))  #formatacao


