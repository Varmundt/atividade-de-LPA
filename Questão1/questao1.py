print('Olá, Bem-vindo a Mauricio Miller Store!')
print('\n| TABELA DE JUROS POR PARCELAS |')
print('1x, 2x ou 3x = 0% de Juros')
print('4x e 5x = 4% de Juros')
print('6x, 7x ou 8x = 8% de Juros')
print('9x, 10x, 11x ou 12x = 16% de Juros')
print('13x ou Mais = 32% de Juros')
valorDoPedido = float(input('\nDigite o Valor do Pedido a ser calculado'))
quantidadeParcelas = int(input('Digite o Numero de Parcelas a serem calculadas'))

#Opções para designar o juros de acordo com o número digitado

if quantidadeParcelas < 4:
    juros = 1.00 #(0/100) ou 0%

elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 1.04 #(4/100) ou 4%

elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 1.08 #(8/100) 8%

elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 1.16 #(16/100) ou 16%

else:
    juros = 1.32 #(32/100) ou 32%

#Calculo do resultado final de acordo com a quantidade de parcelas escolhidas
valorTotalParcelado = valorDoPedido * juros
valorDaParcela = valorTotalParcelado / quantidadeParcelas

#Resultado final
print('O Valor das parcelas é de: R${:.2f}'.format(valorDaParcela))
print('O Valor Total Parcelado é de: R${:.2f}'.format(valorTotalParcelado))