#Exercício 1
dia = input("Digite o nome de um dia da semana: ").lower()

if dia in ["segunda", "terça", "terca", "quarta", "quinta", "sexta"]:
    print("Dia útil")

elif dia in ["sábado", "sabado", "domingo"]:
    print("Fim de semana")

else:
    print("Dia inválido")

#Exercício 2
horario = input("Informe o horário (dia ou noite): ").lower()
caracteristica1 = input("Informe a primeira característica: ").lower()
caracteristica2 = input("Informe a segunda característica: ").lower()

if horario == "noite" and caracteristica1 == "garras" and caracteristica2 == "evita prata":
    print("Lobisomem")

elif horario in ["dia", "noite"] and caracteristica1 == "rápido" and caracteristica2 == "ataca em grupo":
    print("Nekker")

elif caracteristica1 == "não tem olhos" and caracteristica2 == "imita vozes humanas":
    print("Mímico")

else:
    print("Criatura desconhecida. Prepare-se para o pior.")

#Exercício 3
salario = float(input("Informe seu salário: R$ "))

if salario <= 2259.20:
    print("Isento de Imposto de Renda.")
elif salario <= 2826.65:
    imposto = salario * 0.075
    print(f"Imposto de Renda: R$ {imposto:.2f}")
elif salario <= 3751.05:
    imposto = salario * 0.15
    print(f"Imposto de Renda: R$ {imposto:.2f}")
elif salario <= 4664.68:
    imposto = salario * 0.225
    print(f"Imposto de Renda: R$ {imposto:.2f}")
else:
    imposto = salario * 0.275
    print(f"Imposto de Renda: R$ {imposto:.2f}")

#Exercício 4
numero = int(input("Digite um número entre 1 e 100: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Número divisível por 3 e por 5.")
elif numero % 3 == 0:
    print("Número divisível por 3.")
elif numero % 5 == 0:
    print("Número divisível por 5.")
else:
    print("Número comum.")

#Exercício 5
senha = input("Digite uma senha:")

maiscula = False
numero = False
espaco = False

for letra in senha:
    if letra >= 'A' and letra <= 'Z':
        maiuscula = True
    if letra >= '0' and letra <= '9':
        numero = True
    if letra == ' ':
        espaco = True

if len(senha) >= 8 and maiscula and numero and not espaco:
    print("Senha válida!")

else:
    print("Senha inválida. Verifique os seguintes critérios:")
if len(senha) < 8:
    print("Deve ter pelo menos 8 caracteres.")
if not maiscula:
    print("Deve conter pelo menos uma letra maiúscula.")
if not numero:
    print("Deve conter ao menos um número")
if not espaco:
    print("Não pode ter espaço")            
