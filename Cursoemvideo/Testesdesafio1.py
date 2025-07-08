print("Bem-vindo à calculadora de IMC!")
nome = input("Por favor, digite o seu nome: ")
peso = input("Digite o seu peso (em kg): ")
altura = input("Digite a sua altura (em metros): ")
imc = float(peso) / (float(altura) ** 2) # float converte o valor para um número de ponto flutuante
print(f"{nome}, o seu IMC é: {imc:.2f}")
if imc < 18.5:  #Condição para calcular o IMC
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9999999: #elif tras uma ideia de se for verdadeiro, executa o bloco
    print("Você está com o peso normal.")
elif 25 <= imc < 29.9999999:
    print("Você está com sobrepeso.")
elif 30 <= imc < 34.99999:
    print("Você está com obesidade grau 1.")
elif 35 <= imc < 39.99999999:
    print("Você está com obesidade grau 2.")
else: #else é o bloco que executa se nenhuma das condições anteriores forem verdadeiras
    print("Você está com obesidade grau 3 ou mórbida.")
