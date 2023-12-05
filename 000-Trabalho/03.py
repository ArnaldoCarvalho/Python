def quadrado(n):
    return n*n

def cubo(n):
    return n*n*n

def main():
    n = int(input("introduza um número"))
    print(quadrado(n))
    print(cubo(n))
    input()

if __name__ == '__main__':
    main()