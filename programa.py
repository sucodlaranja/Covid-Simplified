import csv


x = input("mete o nome do ficheiro que le\n")
y=input("mete o nome de ficheiro para ser criado\n")

def leitor ():
    with open(x + ".csv",'r') as lido:
        l = ['', '', '', 'Afghasssnistan', '2020-10-27 04:24:45', '33.93911', '67.709953', '40937', '1518', '34150', '5269', 'Afghanistan', '105.15988852440435', '3.7081368932750323']


        reader = csv.reader(lido, quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if(row[3]=='Country_Region'):continue
            if(l[3]=='Afghasssnistan'): l = row
            elif(l[3]==row[3]):
                row=fazcontas(row,l)
                l = row
            else:
                interpretador(l)
                l = row

    interpretador(l)
    lido.close()
    




def fazcontas(l1,l2):
    l1[7] = int(l1[7])+int(l2[7])
    l1[8] = int(l1[8])+int(l2[8])
    l1[9] = int(l1[9]) + int(l2[9])
    return  l1



def interpretador(l) :
        with open(y +".csv",'a+') as escrever:
            writer = csv.writer(escrever,delimiter=';')
            writer.writerow([l[3],l[7], l[8],l[9]])
	

leitor()

escrever.close()