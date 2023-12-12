def main():
    ''' declaração de variáveis '''
    soma = 0
    v = 0
    while(v==0):
        try:  
            x = int(input('Introduza o valor de x: '))
            v=1
        except:
            v=0
            print('O valor têm que ser um numero inteiro')
    v=0
    while(v==0):
        try:
            v=1
            y = int(input('Introduza o valor de y: '))
        except:
            v=0
            print('O valor têm que ser um numero inteiro')

    print('  X  |  Y  ')
    print('-----------')
    while(x>=1):
        mul = x * y
        print(x,' | ',y)
        if(x%2 != 0):
            soma = soma + y
        x = x//2
        y = y*2

  
    print("O resultado da multiplicação é igual:",soma)
    input()


    

if __name__ == '__main__':
    main()