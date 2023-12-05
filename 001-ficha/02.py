''' função principal '''
def main():
    ''' Lê os 3 números '''
    x = float(input("Introduza o primeiro numero"))
    y = float(input("Introduza o segundo numero"))
    z = float(input("Introduza o terceiro numero"))
    ''' Verifica se é um triângulo '''
    if(x+y > z):
        if(x+z > y):
            if(y+z > x):
                print("Forma um triângulo")
            else:
                print("Não forma um triângulo")
        else:
            print("Não forma um triângulo")
    else:
        print("Não forma um triângulo")

    ''' É Utilizado este input para permitir o utilizador ler os dados antes do programa encerrar '''
    input()

''' Chamada do main para ver se ele está funcionando '''
if __name__ == '__main__':
    main()