print("hello World")
#Exercício 1
numero1=float(input("digite o primeiro número"))
numero2=float(input("digite o segundo número"))

print("soma:", numero1 + numero2)
print("subtração:", numero1 - numero2)
print("multiplicação:", numero1 * numero2)
print("divisão:", numero1 / numero2)

#Exercício 2
altura=float(input("digite o tamanho da altura"))
base=float(input("digite o tamanho da base"))
area= (base * altura) / 2
print("Area igual:", area)

#Exercício 3
hora_valor=float(input("Quanto vocÊ ganha por hora?"))
hora_dia=float(input("Quantas horas você trabalha por dia?"))
mes=hora_valor*hora_dia*4*5
print("Salário mensal:", mes)

#Exercício 4
idade=int(input("Digite sua idade"))
dias=idade*365
print("você viveu", dias)

#Exercício 5
nome=input("Diga seu nome:")
sobrenome=input("Diga seu sobrenome")
print("Nome completo:", nome +" "+sobrenome)

#Exercício 6
f = float(input("Digite a temperatura em Fahrenheit: "))
c = (f - 32) * 5/9
k = c + 273.15
print("Celsius:", round(c, 2))
print("Kelvin:", round(k, 2))

#Exercício 7
string_binaria = input("Digite uma string binária (ex: 1011001): ")
quantidade = string_binaria.count('1')
print("Quantidade de 1's:", quantidade)

#Exercício 8
palavra = input("digite uma palavra:")
print("palavra de trás pra frente:", palavra[::-1])

#Exercício 9
frase = input("Digite uma frase: ")
sem_espacos = frase.replace(" ", "")
print("Frase sem espaços:", sem_espacos)

#Exercício 10
frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")

frase1_modificada = frase1[::-1].replace('a', '*').replace('A', '*')
frase2_modificada = frase2[::-1].replace('a', '*').replace('A', '*')

print("Frase 1 modificada:", frase1_modificada)
print("Frase 2 modificada:", frase2_modificada)
