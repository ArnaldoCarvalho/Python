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
        for x in fileS:
            paises.append(fileS[count+1])
            capitais.append(fileS[count+2])
            count = count + 3
        return 1
    except:
        print('erro no carregamento do ficheiro')
        return 0
    
def game():
    if (load()==0):
        return
    vitoria = 0
    load()

    for x in range(4):
        y = random.randint(1,len(paises))
        pais = paises[y]
        capital = capitais[y]

        print('Qual a capital da ', pais)

        poss = random.randint(1,4)

        if poss == 1:
            print('A) ',capital) 
            print('B) ')
            print('C) ')
            print('D) ')
        if poss == 1:
            print('A) ') 
            print('B) ',capital)
            print('C) ')
            print('D) ')
        if poss == 1:
            print('A) ') 
            print('B) ')
            print('C) ',capital)
            print('D) ')
        if poss == 1:
            print('A) ') 
            print('B) ')
            print('C) ')
            print('D) ',capital)


        v = 0
        result = 0
        while v == 0:
            resposta = input("Introduza a letra da opção")
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
            
    return vitoria

''' Chamada do main para ver se ele está funcionando '''
if __name__ == '__main__':
    main()