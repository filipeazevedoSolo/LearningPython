S = 'spammy'

S = S[:3] + 'xx' + S[5:]          #'spa' + 'xx' + 'y'

print(S)

S = 'spammy'

S = S.replace('mm', 'xx')

print(S)

S = 'xxxxSPAMxxxxSPAMxxx'

pos = S.find('SPAM')              #retorna primeira posicao da primeira vez que aparece 'SPAM'

S = S[:pos] + 'EGGS' + S[(pos+4):]

print(S)

S = 'xxxxSPAMxxxxSPAMxxx'

S = S.replace('SPAM', 'EGGS')        #troca todos os 'SPAM' por 'EGGS'

print(S)

S = 'xxxxSPAMxxxxSPAMxxx'

S = S.replace('SPAM', 'EGGS', 1)     #troca apenas um

print(S)

L = ['s','p','a']

S = ''.join(L)                  #junta os elementos todos a lista com '' entre cada

print(S)

line = "The knights who say Ni!\n"

print(line.rstrip())

print(line.endswith('Ni!\n'))

