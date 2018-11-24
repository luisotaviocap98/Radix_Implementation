class No:
    def __init__(self,dado):
        self.dado = dado
        self.listaNos = list()
        self.ePalavra = True

    def __str__(self):
        return self.dado

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
        print('nao precisa fazer nada, sao iguais'.capitalize(),entrada[:match].upper())
        #precisa fazer só quando o atual ePalavra = False
    elif match < len(root.dado) :
        #segundo caso: palavras diferentes
        if match==0:
            print('nao tem nada a ver, criar nó nulo'.capitalize())
            #new=No(none)
            #new.ePalavra=False
            #new.listaNos.append(root,entrada)
        #terceiro caso: prefixo em comum, podendo esse prefixo ser a entrada ou parte dela
        else:
            print('criar nó nulo a cima com palavra nova'.capitalize(),entrada[:match].upper())
            #new=No(entrada[:match])
            #other=No(entrada[match:]) #detalhe para match ser igual o tamanho da entrada
            #other2=No(root[match:])
            #new.listaNos.append(other,other2)
    elif match == len(root.dado):
        #quarto caso: prefixo em comum, sendo esse prefixo o root
        if len(entrada) > len(root.dado):
            print('inseir como filho de root a palavra'.capitalize(),entrada[match:].upper())
            #recursao, precisa verificar na lista de filhos, se possui algum filho com o novo prefixo
            #new=No(entrada[match:])
            #root.listaNos.append(new)
    print()

#base para busca recursiva
#root ='can'
#l=['oa','ta','ario','sao']
#entr=input()
#for i in l:
#    if entr[0] in i:
#        print(i)

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
    addNo(root,'canta')
    addNo(root,'canarinho')
    addNo(root,'corsinha')


if __name__ == "__main__":
    main()
