print('Hello World')

#Exercício 1
NOME='luan'
IDADE='21'
print(f"Meu nome é {NOME} e eu tenho {IDADE} anos")

#Exercício 2
a=5
b=10
a, b = b, a
print(f"a é {a} e b é {b}")

#Exercício 3
PI=3.14159
raio=4
área=PI*(raio**2)
print(f"a área do circulo de raio 4 é {área}")

#Exercício 4
numero=40
numero_dec=4.10
texto='Tudo bem?'
print(type(numero))
print(type(numero_dec))
print(type(texto))

#Exercício 5
calcular=10+5*2-3**2
""" Usando a ordem do ''PEMDAS'' nessa expressão, 
realiza-se primeiro o 3 elevado a 2 (potência), 
seguido da multiplicação, depois adição e subtração
da esquerda para a direita """
print(f"o resultado do calculo é {calcular}")

#Exercício 6
celsius=30
fahrenheit=(celsius*1.8)+32
print(f"A temperatura de {celsius}°C em Fahrenheit é {fahrenheit}°F")

#Exercício 7
x=7
y=4
resul= (x!=y) and (x>0) and (y>0)
print(resul)

#Exercício 8
expressao=(5>3) and (2<1)
print(expressao)
""""A expressão vai ser false, pois ela quer dizer que
5 maior que 3 e 2 menor que 1, para ser true as duas informações
teriam que está em sincronia"""

#Exercício 9
altura_str='1.75'
altura_float= float(altura_str)
print(f" A altura convertida é: {altura_float}")

#Exercício 10
alunos_python= {'Luan','Lis','Livia'}
alunos_java= {'Luan','Rian','Renan'}
duas_ling= alunos_python&alunos_java
so_py= alunos_python-alunos_java
todos_pyja= alunos_java|alunos_python
print(f"Alunos que fazem as duas: {duas_ling}")
print(f"Alunos que só fazem Python: {so_py}")
print(f"Todos os alunos: {todos_pyja}")

