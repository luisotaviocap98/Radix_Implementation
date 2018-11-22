class No:
    def __init__(self):
        self.dado = list()
        self.listaNos = list()
        self.ePalavra = False

    def __str__(self):
        return "OLA "+self.dado

    def addDado(self, novoDado):
        self.dado = novoDado


def main():
    meuNo = No()
    meuNo.addDado("Michel")
    

if __name__ == "__main__":
    main()
