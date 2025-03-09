print(" vamos converter de uma moeda para outra")

vcambio = float(input("Digite o valor do cambio (quantos reais valem 1 dólar): "))
vreal = float(input("Digite o valor em reais (R$): "))

vdolar = vreal / vcambio

print(f"O valor de R${vreal: .2f} em dólares é de US${vdolar: .2f}")