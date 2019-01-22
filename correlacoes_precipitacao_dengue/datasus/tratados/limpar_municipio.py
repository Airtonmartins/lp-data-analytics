entrada = open('dengue_2012.csv','r')

entry = entrada.read()
entrada.close()

first = entry.split('\n')[0]
body = entry.split('\n')[1:]

saida = open('dengue2012.csv','w')
saida.write(first + '\n')

for i in range(len(body)):
    row = body[i]
    row = '"' + row[8:] + '\n'
    saida.write(row)
    
saida.close()
