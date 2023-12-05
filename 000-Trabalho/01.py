def main():
    n = int (input("introduça um número: "))

    if n == 0:
        print("O número é zero")
    else:
        if n%2 == 0:
            print("O número é par")
        else:
            print("O número é impar")
    input("Clique numa tecla para terminar o programa")
if __name__ == '__main__':
    main()