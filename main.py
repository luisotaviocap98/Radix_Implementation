import sys

class No:
    def __init__(self,dado):
        self.dado = dado#reduzido
        self.listaNos = list()
        self.ePalavra = True
        self.pOriginal = dado

def addNo(root, entrada,recurso):
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
            root.pOriginal = entrada
        #print('nao precisa fazer nada, sao iguais'.capitalize(),entrada[:match].upper())

    elif match < len(root.dado) :
        #segundo caso: palavras diferentes
        if match==0:
            #print('nao tem nada a ver, criar nó nulo'.capitalize())
            new=No('')
            new.ePalavra=False
            word = No(entrada)
            word.pOriginal = entrada
            root.pOriginal = root.dado
            new.listaNos.append(root)
            new.listaNos.append(word)
            root = new

        #terceiro caso: prefixo em comum, podendo esse prefixo ser a entrada ou parte dela
        else:
            print('criar nó nulo a cima com palavra nova'.capitalize(),entrada[:match].upper())
            new=No(entrada[:match])  #Nó Acima Cortado


            if match != len(entrada):   #menor
                other=No(entrada[match:]) #detalhe para match ser igual o tamanho da entrada
                other.pOriginal = recurso
                new.listaNos.append(other)

            other2=No(root.dado[match:])
            other2.pOriginal = root.pOriginal.replace("\n", '')
            other2.dado = other2.dado.replace("\n", '')

            other2.ePalavra = root.ePalavra


            for i in root.listaNos:
                i.dado = i.dado.replace("\n", '')
                other2.listaNos.append(i)


            new.listaNos.append(other2)
            new.ePalavra = False
            new.pOriginal = entrada[:match]
            root = new

            #print('\nesse eh o new',new.dado,'esse eh o root',root.dado)
            return root
    elif match == len(root.dado):
        #quarto caso: prefixo em comum, sendo esse prefixo o root

        if len(entrada) > len(root.dado):
            #print('inserir como filho de root a palavra'.capitalize(),entrada[match:].upper())
            #recursao, precisa verificar na lista de filhos, se possui algum filho com o novo prefixo
            flag = False
            if len(root.listaNos) > 0:
                for j,i in enumerate(root.listaNos):
                    if i.dado[0] == entrada[match:][0]:
                        flag =True
                        #print('\nRECURSAO',entrada,'  ',entrada[match:])
                        x=addNo(i,entrada[match:], entrada)
                        x.pOriginal = entrada
                        root.listaNos[j]= x
                        #print('\nTESTE',x.dado,x.listaNos[0].dado,x.listaNos[1].dado,j,root.listaNos[j].dado)

            if len(root.listaNos) == 0 or flag == False:
                new=No(entrada[match:])
                new.pOriginal=entrada
                root.listaNos.append(new)

    print()
    return root

def imprimindoAll(root):
    if(len(root.listaNos)!=0):
        for i in root.listaNos:
            if i.ePalavra == True:
                print('[', end='')
                print(i.pOriginal, end='')
                print(']',end='')
        for i in root.listaNos:
            imprimindoAll(i)


def imprimindo(root):
    if(len(root.listaNos)!=0):
        print('\n*',root.dado,root.ePalavra)
        for i in root.listaNos:
            print('[', end='')
            print(i.dado,'*',i.ePalavra,'*' ,end='')
            print(']',end='')
        for i in root.listaNos:
            imprimindo(i)


def buscando(root, prefixo):

    #print(prefixo[ len(root.pOriginal[:len(prefixo)] ):])
    if root.pOriginal[:len(prefixo)] in prefixo:
        if root.ePalavra == True and len(root.pOriginal) >= len(prefixo):
            print(root.pOriginal)
        if len(root.listaNos)>0:
            for i in root.listaNos:
                buscando(i,prefixo)

def main():
    arq = sys.argv[1]
    f = open(arq, 'r')
    line = f.readline().lower() #Linha 1 - root
    root = No(line)
    for line in f:
        trans = line.replace("\n", '').lower()
        print('trans ', trans)
        root = addNo(root,trans, trans)

    print('\n--------PRINT Todos---------------')
    imprimindoAll(root)
    print()

    print('\n--------PRINT com Nos---------------')
    imprimindo(root)
    print()

    print('\n-------BUSCANDO------')
    buscando(root, "can")

if __name__ == "__main__":
    main()
