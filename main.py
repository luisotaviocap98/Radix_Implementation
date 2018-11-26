import sys

class No:
    def __init__(self,dado):
        self.dado = dado#reduzido
        self.listaNos = list()
        self.ePalavra = True
        self.pOriginal = None


def addNo(root, entrada):
    #percorrer as duas string para conferir compatibilidades
    match=0
    for i in range(0,len(entrada)):
        if i<len(root.dado) :
            if entrada[i]!=root.dado[i] :
                #se possuem diferenças entre as strings
                break
            else:
                match+=1
        else:
            #se ultrapssou o tamanho da string dado em root
            break

    #mostrar a entrada , o root, ate que posiçao percorreu nas string, e qual atitude a ser tomada
    print('entrada',entrada.upper(),'root'.rjust(14-len(entrada)),root.dado.upper(),'resultado:'.rjust(12),end=' ')
    #4 casos :
    #primeiro caso: inserindo uma palavra que ja existe na arvore
    if entrada == root.dado:
        if(root.ePalavra == False):
            root.ePalavra = True
        if(root.ePalavra == True):
            print('mudou ou ja era true',end= '     ')
        print('nao precisa fazer nada, sao iguais'.capitalize(),entrada[:match].upper())

        #precisa fazer só quando o atual ePalavra = False
    elif match < len(root.dado) :
        #segundo caso: palavras diferentes
        if match==0:
            print('nao tem nada a ver, criar nó nulo'.capitalize())
            new=No(None)
            new.ePalavra=False
            word = No(entrada)
            new.listaNos.append(root)
            new.listaNos.append(word)
            root = new
            '''
            for i in root.listaNos:
                print(i.dado)
                for j in i.listaNos:
                    print(j.dado)
            '''
        #terceiro caso: prefixo em comum, podendo esse prefixo ser a entrada ou parte dela
        else:
            print('criar nó nulo a cima com palavra nova'.capitalize(),entrada[:match].upper())
            new=No(entrada[:match])
            print('\nMATCH ',match,'LEN',len(entrada),'NEW',new.dado)
            if match != len(entrada):   #menor
                other=No(entrada[match:]) #detalhe para match ser igual o tamanho da entrada
                new.listaNos.append(other)




                # vai ter que ter recursão
                print('11111',other.dado)
            other2=No(root.dado[match:])

            for i in root.listaNos:
                other2.listaNos.append(i)

            #    print('NoGravado ',i.dado)
            print('22222',other2.dado)
            #print()
            #print('Tamanho ',len(other2.listaNos))
            #print('Nós ',other2.listaNos[1])


            #print("Dado de Other2: ", other2.dado)
            new.listaNos.append(other2)
            root = new

            print('\nesse eh o new',new.dado,'esse eh o root',root.dado)
            root.ePalavra = False
            return root
    elif match == len(root.dado):
        #quarto caso: prefixo em comum, sendo esse prefixo o root

        if len(entrada) > len(root.dado):
            print('inserir como filho de root a palavra'.capitalize(),entrada[match:].upper())
            #recursao, precisa verificar na lista de filhos, se possui algum filho com o novo prefixo
            flag = False
            if len(root.listaNos) > 0:
                for j,i in enumerate(root.listaNos):
                    if i.dado[0] == entrada[match:][0]:
                        flag =True
                        print('\nRECURSAO',entrada,'  ',entrada[match:])
                        x=addNo(i,entrada[match:])
                        print('\nTESTE',x.dado,x.listaNos[0].dado,x.listaNos[1].dado,j,root.listaNos[j].dado)
                        root.listaNos[j]=x

            if len(root.listaNos) == 0 or flag == False:
                new=No(entrada[match:])
                root.listaNos.append(new)
        #print(root.listaNos[0].dado)
    print('\nolha o root',root.dado)
    print()
    return root

def imprimindo(root):
    print(root.dado)
    if(len(root.listaNos)>0):
        for i in root.listaNos:
            imprimindo(i)
def main():

    #root = No('canto')
    #root = addNo(root,'cano')
    #root = addNo(root,'canario')
    #root = addNo(root,'cantoria')
    #root = addNo(root,'carro')


    arq = sys.argv[1]
    f = open(arq, 'r')
    line = f.readline() #Linha 1 - root
    root = No(line)
    for line in f:
        trans = line.replace("\n", '')
        print('trans ', trans)
        root = addNo(root,trans)

    imprimindo(root)
    #print(root.dado,root.listaNos[0].dado,root.listaNos[1].dado)
    #print('qnt tem',len(root.listaNos))
    #print('\n ROOT',root.dado)
    #print('listnos[0] ', root.listaNos[0].dado)
    #print('listnos[1] ', root.listaNos[1].dado)
    #print('listnos[1] ', root.listaNos[2].dado)
    #print('listnos FILHO ', root.listaNos[1].listaNos[0].dado)
    #print('listnos FILHO e root',root.dado, root.listaNos[1].listaNos[0].dado)#.listaNos[1].dado)
    #print('listnos FILHO ', root.listaNos[1].listaNos[1].listaNos[0].dado)
    #print('listnos FILHO ', root.listaNos[1].listaNos[2].dado)


    #print('\n ROOT-Filho[0]',root.listaNos[0].dado)
    #print('\n ROOT-Filho[1]',root.listaNos[1].dado)
    #print('\n ROOT-Filho[1]',root.listaNos[1].listaNos[0])
    #print('\n ROOT-Filho[2]',root.listaNos[2].dado)
    #print('\n ROOT-Filho[2]',root.listaNos[2].dado)

if __name__ == "__main__":
    main()
