import random
''' função principal '''
paises = []
capitais = []

def main():
    
    input('Introduza qualquer digito para iniciar o jogo ')
    vitoria = 0
    vitoria = game() 
    print(' Parabéns acertou ',vitoria, ' respostas')
    
    ''' É Utilizado este input para permitir o utilizador ler os dados antes do programa encerrar '''
    input()

def game():
    vitoria = 0
    return vitoria

''' Chamada do main para ver se ele está funcionando '''
if __name__ == '__main__':
    main()