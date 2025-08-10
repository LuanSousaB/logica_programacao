#Atividade 1
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Atividade 2
numero = int(input("Digite um número para calcular o fatorial: "))
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
       resultado *= i
    return resultado

resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")    

#Atividade 3 X

#Atividade 4
print("Digite os números inteiros ('fim' para encerrar):")
n = input("Digite um número: ")

while n != 'fim':
    numero = int(n)
    if numero % 2 != 0:
       print(numero)
    n = input("Digite um número: ")

print("Fim da sequência.")

#Atividade 5
print("Digite os números inteiros ('fim' para encerrar):")
n = input("Digite um número: ")

quantidade_negativos = 0

while n != 'fim':
    numero = int(n)
    if numero < 0:
       quantidade_negativos += 1
    n = input("Digite um número: ")


print(f"Quantidade de números negativos: {quantidade_negativos}")

#Atividade 6
print("Bem-vindo ao desafio da adivinhação!")
print("Eu escolhi um número entre 1 e 100, e você tem que descobri-lo!")


while True:
    tentativa = int(input("Chuta um número: "))
    tentativas += 1  
    if tentativa < numero_secreto:
        print("O número que eu escolhi é maior, tente novamente.")
    elif tentativa > numero_secreto:
        print("O número que eu escolhi é menor, tente novamente.")
    else:
        print(f"Você acertou! O número era {numero_secreto}.")
        print(f"Você precisou de {tentativas} tentativas para descobrir!")
        break

#Atividade 7
frase = input("Escreva uma frase: ")

vogais = "aeiouAEIOU"

quantidade_vogais = 0

for letra in frase:
    quantidade_vogais += 1


print(f"Na sua frase, existem {quantidade_vogais} vogais.")