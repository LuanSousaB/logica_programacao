#ATIVIDADE 1

palavras = []
contador = 0

while contador < 10:
    palavra = input(f"Digite a palavra {contador + 1}: ")
    palavras.append(palavra)
    contador += 1

print("\nLista na ordem inversa:")
for i in range(len(palavras) - 1, -1, -1):
    print(palavras[i])

for i in range(len(palavras)):
    if palavras[i].startswith('a') or palavras[i].startswith('A'):
        palavras[i] = '***'


print("\nLista modificada (palavras com 'a' substituídas):")
for palavra in palavras:
    print(palavra)


#ATIVIDADE 2

alunos = {}
contador = 0

while contador < 5:
    nome = input(f"\nDigite o nome do aluno {contador + 1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota
    contador += 1


print("\nNotas dos alunos:")
for nome in alunos:
    print(f"{nome}: {alunos[nome]}")


soma = 0
for nota in alunos.values():
    soma += nota

media = soma / 5
print(f"\nMédia da turma: {media:.2f}")


maior_nota = -1
melhor_aluno = ""

for nome in alunos:
    if alunos[nome] > maior_nota:
        maior_nota = alunos[nome]
        melhor_aluno = nome

print(f"\nAluno com maior nota: {melhor_aluno} ({maior_nota})")


#ATIVIDADE 3

"""
Tupla:
- Imutável (não pode ser alterada depois de criada)
- Usa parênteses: ()
- Ex: frutas = ("maçã", "banana")

Lista:
- Mutável (pode adicionar, remover e alterar valores)
- Usa colchetes: []
- Ex: lista = ["maçã", "banana"]

Dicionário:
- Armazena pares de chave e valor
- Usa chaves: {}
- Ex: aluno = {"nome": "João", "nota": 8.5}
"""


#ATIVIDADE 4

frutas = ("banana", "maçã", "uva", "laranja", "maçã", "melancia", "uva")

fruta = input("\nDigite o nome de uma fruta: ")


quantidade = 0
for item in frutas:
    if item == fruta:
        quantidade += 1

print(f"\nA fruta '{fruta}' aparece {quantidade} vez(es) na tupla.")


if fruta in frutas:
    for i in range(len(frutas)):
        if frutas[i] == fruta:
            print(f"Primeira ocorrência no índice: {i}")
            break
else:
    print("A fruta não foi encontrada na tupla.")
