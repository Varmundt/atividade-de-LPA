print('\nSeja Bem-Vindo ao Mauricio Miller Marmitas!')
print('|---------------------| Menu do Dia |-----------------------|')
print('*-----------------------------------------------------------*')
print('|  Tamanho  | Bife Acebolado (BA)  |  Filé de Frango (FF)   |')
print('|-----------|----------------------|------------------------|')
print('|   - P -   |       R$ 16.00       |       R$ 15.00         |')
print('|   - M -   _       R$ 18.00       _       R$ 17.00         |')
print('|   - G -   |       R$ 22.00       |       R$ 21.00         |')
print('*-----------------------------------------------------------*')

total = 0.0 # Variavel usada para somar o valor final dos produtos

bifeP = 16.00
bifeM = 18.00
bifeG = 22.00
            # Acima e abaixo a lista das Variaveis usadas para definir o preço dependendo do tamanho e sabor
fileP = 15.00
fileM = 17.00
fileG = 21.00

while True:

# Escolhe um Sabor e em seguida pergunta o Tamanho
    while True:
        sabor = input("Entre com o sabor desejado (BA/FF): ")
        if sabor == "BA":
            tamanho = input("Entre com o tamanho desejado (P/M/G): ")
            if tamanho == "P":
                preco = bifeP
                print("Você pediu um Bife Acebolado no tamanho P: R$ {}".format(preco))
                total += preco
                break
            elif tamanho == "M":
                preco = bifeM
                print("Você pediu um Bife Acebolado no tamanho M: R$ {}".format(preco))
                total += preco
                break
            elif tamanho == "G":
                preco = bifeG
                print("Você pediu um Bife Acebolado no tamanho G: R$ {}".format(preco))
                total += preco
                break
            else:
                print("\nTamanho inválido. Tente novamente.")

        elif sabor == "FF":
            tamanho = input("Entre com o tamanho desejado (P/M/G): ")
            if tamanho == "P":
                preco = fileP
                print("Você pediu um Filé de Frango no tamanho P: R$ {}".format(preco))
                total += preco
                break
            elif tamanho == "M":
                preco = fileM
                print("Você pediu um Filé de Frango no tamanho M: R$ {}".format(preco))
                total += preco
                break
            elif tamanho == "G":
                preco = fileG
                print("Você pediu um Filé de Frango no tamanho G: R$ {}".format(preco))
                total += preco
                break
            else:
                print("\nTamanho inválido. Tente novamente.")
        else:
            print("\nSabor inválido. Tente novamente.")

# Repete o ciclo caso queira comprar mais coisas
    mais = input("Deseja mais alguma coisa? (S/N): ")
    if mais == "S":
        continue
    elif mais == "N":
        break

# Mostra a Soma total
print("\nO valor total a ser pago: R$ {:.2f}".format(total))