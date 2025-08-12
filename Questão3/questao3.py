print("Olá, Bem-vindo a Fábrica de Camisetas do Mauricio Miller")
def escolha_modelo():
# Variavel que define o valor do modelo de acordo com a opção escrita
    modCamisa = {"MCS": 1.80,"MLS": 2.10,"MCE": 2.90, "MLE": 3.20}
    while True:
        print("\nEntre com o modelo desejado")
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Com Estampa")
        print("MLE - Manga Longa Com Estampa")
        modelo = input(">>")
        if modelo in modCamisa:
            return modCamisa[modelo], modelo
        else:
            print("Escolha inválida, entre com o modelo novamente")
def num_camisetas():
# Variavel para o numero de camisetas e Descontos
    while True:
        try:
            quantidade = int(input("\nEntre com o número de camisetas: "))
            if quantidade > 20000:
                print("Não aceitamos tantas camisetas de uma vez.")
                continue
            if quantidade < 20:
                return quantidade
            elif 20 <= quantidade < 200:
                return int(quantidade * 0.95)
            elif 200 <= quantidade < 2000:
                return int(quantidade * 0.93)
            elif 2000 <= quantidade <= 20000:
                return int(quantidade * 0.88)
        except ValueError:
            print("Valor inválido, digite um número inteiro.")
def frete():
# Variavel que define o valor do frete de acordo com as opções
    opFrete = {"1": 100.00,"2": 200.00,"0": 0.00}
    while True:
        print("\nEscolha o tipo de frete:")
        print("1 - Frete por transportadora - R$ 100.00")
        print("2 - Frete por Sedex - R$ 200.00")
        print("0 - Retirar pedido na fábrica - R$ 0.00")
        escFrete = input(">>")
        if escFrete in opFrete:
            return opFrete[escFrete]
        else:
            print("Opção inválida, tente novamente.")

        # MAIN

modelo, modelo2 = escolha_modelo()
numcamisas = num_camisetas()
frete = frete()
# Variavel para calcular o total
total = (modelo * numcamisas) + frete

print("\nTotal: R$ {} (Modelo: {} * Quantidade(com desconto): {} + frete: {})".format(total, modelo, numcamisas, frete))