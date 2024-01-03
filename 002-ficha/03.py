''' função principal '''
def main():
    x = input(" Introduça uma String: ")
    tamanho = x.split(' ')
    print(" Nesta string existem: ",len(tamanho)-1," espaços")
    ''' É Utilizado este input para permitir o utilizador ler os dados antes do programa encerrar '''
    input()

''' Chamada do main para ver se ele está funcionando '''
if __name__ == '__main__':
    main()