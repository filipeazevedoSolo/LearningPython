S = 'spam'

for (pos,item) in enumerate(S):                      #enumerate -> (0,s)
    print(item, '->', pos)

#file iterator

for line in open('teste.txt'):
    print(line, end='')

#iterator
L = [1,2,4]
I = iter(L)
print('\n',next(I))


E = enumerate('spam')
I = iter(E)
print(next(I))
print(list(E))

for i in range(len(L)):               #igual a for(i=0; i<3...)
    L[i]+=10
print(L)

L = [x + 10 for x in L]               #mais eficiente
print(L)

lines = [line.rstrip() for line in open('teste.txt')]
print(lines)

print([x + y for x in 'abc' for y in 'lmn'])        #todas as combinações de concatenação
