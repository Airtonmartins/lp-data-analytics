entrada = open('dengue2012.csv','r')
entry = entrada.read()
entrada.close()

entry = entry.replace('á', 'a')
entry = entry.replace('â', 'a')
entry = entry.replace('ã', 'a')
entry = entry.replace('à', 'a')
entry = entry.replace('Á', 'A')
entry = entry.replace('Â', 'A')
entry = entry.replace('Ã', 'A')
entry = entry.replace('À', 'A')
entry = entry.replace('é', 'e')
entry = entry.replace('ê', 'e')
entry = entry.replace('è', 'e')
entry = entry.replace('É', 'E')
entry = entry.replace('Ê', 'E')
entry = entry.replace('È', 'E')
entry = entry.replace('í', 'i')
entry = entry.replace('î', 'i')
entry = entry.replace('ì', 'i')
entry = entry.replace('Í', 'I')
entry = entry.replace('Î', 'I')
entry = entry.replace('Ì', 'I')
entry = entry.replace('ó', 'o')
entry = entry.replace('ô', 'o')
entry = entry.replace('õ', 'o')
entry = entry.replace('ò', 'o')
entry = entry.replace('Ó', 'O')
entry = entry.replace('Ô', 'O')
entry = entry.replace('Õ', 'O')
entry = entry.replace('Ò', 'O')
entry = entry.replace('ú', 'u')
entry = entry.replace('û', 'u')
entry = entry.replace('ù', 'u')
entry = entry.replace('Ú', 'U')
entry = entry.replace('Û', 'U')
entry = entry.replace('Ù', 'U')
entry = entry.replace('ç', 'c')
entry = entry.replace('ç', 'C')

def maiusculo(x):
    if(x.isnumeric() == False):
        x = x.upper()
        return x
    else:
        return x

string = ''
for i in range(len(entry)):
    string += maiusculo(entry[i])


saida = open('dengue2012_2.csv','w')
saida.write(string)
saida.close()

