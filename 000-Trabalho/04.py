def main():
    c = int(input("introduça um número: "))
    n = 1
    while c > 0:
        c = int(input("introduza um número: "))
        n = n + 1
    print("Total: ", n)
    input()

if __name__ == '__main__':
    main()