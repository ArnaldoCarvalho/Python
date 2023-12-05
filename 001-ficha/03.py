''' função principal '''
def main():
    ''' Lê os 3 números '''
    x = float(input("Introduza o primeiro numero"))
    y = float(input("Introduza o segundo numero"))
    z = float(input("Introduza o terceiro numero"))
    ''' Verifica se é um triângulo e o tipo de triângulo'''
    if(x+y > z):
        if(x+z > y):
            if(y+z > x):
                print("Forma um triângulo")
                if( x == y):
                    if(x == z):
                        print('equilátero')
                    else:
                        print('isosceles')
                else:
                    if(y == z):
                        print('isosceles')
                    else:
                        if(x == z):
                            print('isosceles')
                        else:
                            print('escaleno')
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