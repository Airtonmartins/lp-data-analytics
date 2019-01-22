entrada = open('all_cities_dengue.csv','r')

head = entrada.readline()
head = '"MUNICIPIO";"ANO";"MES";"CASOS"\n'

saida = open('all_dengue.csv','w')
saida.write(head)

body = entrada.read().split('\n')
entrada.close()
tamanho1 = len(body)

for i in range(tamanho1):
    row = body[i].split(';')
    #print(row)
    city = row[0]
    #print(city)
    year = row[1]
    #print(year)
    row = row[2:]
    #print(row)
    for month in range(len(row)):
        #print(month)
        saida.write(city + ';' + year + ';' + str(month + 1) + ';' + row[month] + '\n')

saida.close()




