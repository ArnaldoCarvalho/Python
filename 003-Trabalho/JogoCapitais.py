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

def randomC(capitais2):
    v = 0
    while v == 0:
        n = random.randint(0,len(paises)-1)
        if capitais2[n] != '':
            v=1
            return n
    return 0

def randomY(capitaisUse):
  v = 0
  y = 0
  while v == 0:
      v = 1
      y = random.randint(0,len(paises)-1)
      for x in range(len(capitaisUse)):
          if capitaisUse[x]==capitais[y]:
              v=0
  return y 

def game():
    if (load()==0):
        print("Aconteceu um erro no carregamentos dos paises e capitais para o jogo")
        return 0
    vitoria = 0
    capitais2 = []
    capitaisUse = []
    i=0
    y=0
    while i != 4:

        if i != 0:
            y=randomY(capitaisUse)
            pais = paises[y]
            capital = capitais[y]
        else:
            y = random.randint(0,len(paises)-1)
            pais = paises[y]
            capital = capitais[y]

        capitais2 = capitais.copy()
        capitais2[y]= ''
        print("Qual a capital da ", pais)
        capitaisUse.append(capitais[y])

        poss = random.randint(1,4)
        n=0
        if poss == 1:
            print("A ",capital) 
            n = randomC(capitais2)
            print("B ",capitais2[n])
            capitais2[n]=''
            n = randomC(capitais2)
            print("C ",capitais2[n])
            capitais2[n]=''
            n = randomC(capitais2)
            print("D ",capitais2[n])
            capitais2[n]=''
        if poss == 2:
            n = randomC(capitais2)
            print("A ",capitais2[n]) 
            capitais2[n]=''
            print("B ",capital)
            n = randomC(capitais2)
            print("C ",capitais2[n])
            capitais2[n]=''
            n = randomC(capitais2)
            print("D ",capitais2[n])
            capitais2[n]=''
        if poss == 3:
            n = randomC(capitais2)
            print("A ",capitais2[n]) 
            capitais2[n]=''
            n = randomC(capitais2)
            print("B ",capitais2[n])
            capitais2[n]=''
            print("C ",capital)
            n = randomC(capitais2)
            print("D ",capitais2[n])
            capitais2[n]=''
        if poss == 4:
            n = randomC(capitais2)
            print("A ",capitais2[n]) 
            capitais2[n]=''
            n = randomC(capitais2)
            print("B ",capitais2[n])
            capitais2[n]=''
            n = randomC(capitais2)
            print("C ",capitais2[n])
            capitais2[n]=''
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