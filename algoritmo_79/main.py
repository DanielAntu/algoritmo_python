print('='*60)
print('\t==== Rendimento de aplicações ====')
print('='*60)
p = float(input('Digite o valor da aplicação: '))
i = float(input('Digite a taxa: '))
m = int(input('Digite o número de meses: '))
print('='*60)
valor = p*(((1+i)**m)-1)/i
print()
print('='*60)
print(f'Valor acumulado: R${valor:.2f}')
print('='*60)
