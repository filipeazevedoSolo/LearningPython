engineers = {'bob','sue','ann','vic'}
managers = {'tom','sue'}

print('bob' in engineers)       #retorna true se tiver no set

print(engineers & managers)     #retorna quem pertence aos dois grupos

print(engineers | managers)     #retorna todas as pessoas dos dois grupos

print(engineers - managers)     #engenheiros que nao sao managers

print(engineers > managers)     #retorna true se todos os managers forem engenheiros

print({'bob','sue'} < engineers)   #retorna true se ambos forem engenheiros

print((managers | engineers) > managers)  #todos os elementos de manager estao em 'toda a gente'

print(managers ^ engineers)       #quem esta num grupo mas nao nos dois


