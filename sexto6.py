import os 
#Faça um programa que leia um número inteiro e exiba a sequência de Fibonacci até o enésimo termo (onde n é o número lido).

numero = int(input("Digite um número inteiro: "))
fibonacci = [0, 1]

for i in range(2, numero):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("A sequência de Fibonacci até o", numero, "º termo é:")
for i in range(numero):
    print(fibonacci[i], end=" ")

os.system("pause")