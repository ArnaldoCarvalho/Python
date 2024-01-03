''' função principal '''
def main():

    ''' É Utilizado este input para permitir o utilizador ler os dados antes do programa encerrar '''
    pais = (input('Introduza um país: '))    
    print('A capital do país introduzido é:',dicionario(pais)) 
    
    input()


def dicionario(pais):
    capital = {'França':'Paris','Portugal':'Lisboa','Espanha':'Madrid','Luxemburgo':'Luxemburgo'}
    for x in capital:  
        if (x == pais):
            return capital[x]
    return 'não foi encontrada a capital desse país'

''' Chamada do main para ver se ele está funcionando '''
if __name__ == '__main__':
    main()