#7 - calculo do IMC

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura ** 2)

print("O seu IMC é: ", imc)
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 24.9:
    print("Você está com o peso normal.")
elif imc >= 25 and imc < 29.9:
    print("Você está com sobrepeso.")
elif imc >= 30 and imc < 34.9:
    print("Você está com obesidade grau 1.")
elif imc >= 35 and imc < 39.9:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3.")