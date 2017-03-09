file = open('ficheiro_teste.txt','w')

file.write('linha de teste 1\n')

file.write('linha de teste 2\n')

file.close()

for line in open('ficheiro_teste.txt'):              #file iterator
    print(line)

file = open('data.bin', 'rb').read()   #rb = read binary

print(file)

print(file[4:8])

print(file[0])

print(bin(file[0]))

X,Y,Z = 43, 44, 45
D={'a':1, 'b':2}
L=[1,2,3]

F = open('datafile.txt','w')
F.write('%s,%s,%s\n' % (X,Y,Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

chars = open('datafile.txt','r').readline()
print(chars)
chars = chars.rstrip()
print(chars)
Sp = eval(chars)           #converte para qualquer tipo de objeto
print(Sp)
X = Sp[0]
print(X)