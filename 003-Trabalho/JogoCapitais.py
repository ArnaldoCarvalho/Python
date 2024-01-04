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

def load():
    try:
        file = open('./text.txt','r')
        fileS = file.read().split('|')
        count = 0
        for i in fileS:
            if count+1 >= len(fileS):
                return 1
            paises.append(fileS[count+1])
            capitais.append(fileS[count+2])
            count = count + 3
        return 1
    except:
        print('erro no carregamento do ficheiro')
        return 0
    
def game():
    if (load()==0):
        print("Aconteceu um erro no carregamentos dos paises e capitais para o jogo")
        return 0
    vitoria = 0

    i=0
    while i != 4:
        y = random.randint(1,len(paises))
        pais = paises[y]
        capital = capitais[y]
        
        print("Qual a capital da ", pais)

        poss = random.randint(1,4)
        if poss == 1:
            print("A ",capital) 
            print("B ")          
            print("C ")
            print("D ")
        if poss == 2:
            print("A ") 
            print("B ",capital)
            print("C ")
            print("D ")
        if poss == 3:
            print("A ") 
            print("B ")
            print("C ",capital)
            print("D ")
        if poss == 4:
            print("A ") 
            print("B ")
            print("C ")
            print("D ",capital)


        v = 0
        result = 0
        while v == 0:
            resposta = input("Introduza a letra da opção: ")
            resposta = resposta.upper()

            if resposta == 'A':
                result = 1
                v=1
            else:
                if resposta == 'B':
                    result = 2
                    v=1
                else:
                    if resposta == 'C':
                        result = 3
                        v=1
                    else:
                        if resposta == 'D':
                            result = 4
                            v=1
                        else:
                            v=0
        
        if result == poss:
            vitoria = vitoria + 1
            print("Resposta Certa")
        else:
            print("Resposta Errada")
        i = i+1

    return vitoria
        
        
''' Chamada do main para ver se ele está funcionando '''
if __name__ == '__main__':
    main()