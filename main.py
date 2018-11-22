class No:
    def __init__(self,dado):
        self.dado = dado
        self.listaNos = list()
        self.ePalavra = True

    def __str__(self):
        return self.dado

def addNo(root, entrada):
    if entrada in root.dado:
        print(entrada,'é prefixo de',root.dado)
    elif root.dado in entrada:
        print(root.dado, 'é prefixo de ',entrada)

    # if entrada in i:
    #     print(entrada,' prefixo de ',y)
    #     for i in entrada:
    #         k+=1
    #     j=y[k:]
    #     t=y[:k]
    #     print(j,' e ',t)
    # elif y in entrada:
    #     print(y,' prefixo de ',entrada)
    # else:
    #     print('incompativeis')


def main():
    root = No("recanto")
    print(root)
    addNo(root,"canto")


if __name__ == "__main__":
    main()
