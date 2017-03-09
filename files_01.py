f = open('teste.txt','w')
f.write('Hello\n')
f.write('Goodbye')
f.close()

f=open('teste.txt')
text = f.read()
f.close()
print(text)
