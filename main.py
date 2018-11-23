class No:
    def __init__(self,dado):
        self.dado = dado
        self.listaNos = list()
        self.ePalavra = True

    def __str__(self):
        return self.dado

def addNo(root, entrada):
    #percorrer as duas string para conferir compatibilidades
    for i in range(0,len(entrada)):
        if i<len(root.dado) :
            if entrada[i]!=root.dado[i] :
                #se possuem diferenças entre as strings
                break
        else:
            #se ultrapssou o tamanho da string dado em root
            break

    #mostrar a entrada , o root, ate que posiçao percorreu nas string, e qual atitude a ser tomada
    print('entrada',entrada.upper(),'root',root.dado.upper(),'foi ate pos',i,'resultado:',end=' ')
    #4 casos :
    if i < len(root.dado) :
        #primeiro caso: palavras diferentes
        if i==0:
            print('nao tem nada a ver, criar nó nulo')
        #segundo caso: inserindo uma palavra que ja existe na arvore
        elif entrada == root.dado:
            print('nao precisa fazer nada, sao iguais')
        #terceiro caso: prefixo em comum, podendo esse prefixo ser a entrada ou parte dela
        else:
            print('criar nó a cima com palavra nova',entrada[:i].upper())

    elif i == len(root.dado):
        #quarto caso: prefixo em comum, sendo esse prefixo o root
        if len(entrada) > len(root.dado):
            print('inseir como filho de root a palavra',entrada[i:].upper())
    print()



def main():
    root = No('canto')
    #primeiro caso
    addNo(root,'aviao')
    #segundo caso
    addNo(root,'canto')
    #terceiro caso
    addNo(root,'canoa')
    #quarto caso
    addNo(root,'cantor')

    #mais exemplos
    addNo(root,'cantora')
    addNo(root,'cantoria')
    addNo(root,'canarinho')


if __name__ == "__main__":
    main()
