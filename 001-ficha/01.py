
''' função principal '''
def main():
    ''' Lês o 3 números '''
    x = int(input("Introduza o primeiro numero"))
    y = int(input("Introduza o segundo numero"))
    z = int(input("Introduza o terceiro numero"))
    ''' Verifica qual o maior número'''
    if(x>y):
        if(x>z):
            print('O maior é: ', x)
        else:
            print('O maior é: ', z)
    else:
        if(y>z):
             print('O maior é: ', y)
        else:
             print('O maior é: ', z)
    ''' É Utilizado este input para permitir o utilizador ler os dados antes do programa encerrar '''
    input()

''' Chamada do main para ver se ele está funcionando '''
if __name__ == '__main__':
    main()