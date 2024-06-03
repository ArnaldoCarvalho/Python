''' função principal '''
def main():
    '''Chama a função menu que irá retornar um resultado'''
    result = menu()
    '''Este print é responsável por mostrar os resultados devolvidos pela função menu'''
    print(menu().__doc__)
    print(result)
    ''' É Utilizado este input para permitir o utilizador ler os dados antes do programa encerrar '''
    input()


def menu():
    '''variáveis necessárias para o bom funcionamento do programa.'''
    menor = 0
    soma = 0
    n = 1
    ''' Ciclo que termina apenas quando o utilizador introduzir um 0 ou a soma ser igual ou menor que -50'''
    while(n!=0 and soma > -50):
        ''' Ciclo que garante que a pessoa introduz um número '''
        v = 0
        while(v==0):
            ''' Verifica se realmente foi introduzido um número e evita que o programa gere um erro. caso não seja um numero dá um aviso '''
            try:
                '''leitura e conversão para inteiro do valor introduzido'''
                n = int(input("Introduza um número: "))
                v=1
            except:
                print("Tem que ser um número")
                v=0
        
        ''' verifica se o número introduzido não é positivo se não for soma, se for apenas ignora'''
        if n <= 0:
            soma = soma + n
        ''' verifica se o número introduzido é menor que o anterior '''
        if menor > n:
            menor = n
    
    ''' verifica se a soma é menor ou igual a -50 e retorna uma mensagem, se for menor devolve o menor número, se for maior retorna o valor da soma'''
    if(soma <= -50):
        return " O menor dos valores lidos é: "+ str(menor)
    else:
        return " O somatório dos valores negativos lidos é: " + str(soma)

''' Chamada do main para ver se ele está funcionando '''
if __name__ == '__main__':
    main()