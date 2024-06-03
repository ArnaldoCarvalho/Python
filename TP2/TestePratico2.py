''' função principal '''
def main():
    '''Variáveis necessárias ao funcionamento do programa'''
    ''' A variável 'n' guarda o valore introduzido '''
    n = 0
    ''' A variável 'soma' guarda o valore da soma de todos os valores positivos não divisiveis por 3 '''
    soma = 0
    ''' A variável 'count ' guarda a quatidade de números positivos não divisiveis por 3 '''
    count = 0
    ''' A variável 'v' conta quantos número já foram introduzidos '''
    v = 0
    
    '''ciclo para fazer a leitura e preparação dos dados'''
    while n >= 0 or v < 9:
        try:
            n = int(input('Introduza um número: '))
            if n > 0:
                if n%3 != 0:    
                    count = count + 1
                    soma = soma + n

            v = v + 1
        except:
            print(" O valor introduzido tem que ser um número")

    ''' verifica se for introduzidos 9 numeros, verdade print média senão mostra quantos foram introduzidos'''
    if v == 9:
      if count > 0:
        mediax = media(soma,count)
        print(" A média dos valores positivos não divísiveis por 3 é: ", mediax)
      else:
        print("Não foi possível calcular a média, pois count é igual a zero")
    else:
        print(" O número de valores positivos não divisíveis por 3 é: ",count)

    print(media,__doc__)
    ''' É Utilizado este input para permitir o utilizador ler os dados antes do programa encerrar '''
    input()

'''<function media at 0x000002572318D300>  função principal
A função média recebe 2 variáveis (soma e count) retornando a média
'''
def media(soma,count):
  return round(soma/count,2)

''' Chamada do main para ver se ele está funcionando '''
if __name__ == '__main__':
    main()