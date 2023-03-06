import os 
# Faça um programa que leia um número inteiro e exiba todos os números perfeitos menores ou iguais a ele. Um número é perfeito se a soma de seus divisores (exceto ele próprio) é igual a ele.

numero = int(input("Digite um número inteiro: "))

for i in range(1, numero+1):
    soma_divisores = 0
    for j in range(1, i):
        if i % j == 0:
            soma_divisores += j
    if soma_divisores == i:
        print(i, "é um número perfeito")

os.system("pause")