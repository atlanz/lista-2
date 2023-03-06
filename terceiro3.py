import os 
# Faça um programa que leia um número inteiro e exiba todos os números primos menores ou iguais a ele.


numero = int(input("Digite um número inteiro: "))

print("Números primos menores ou iguais a", numero, ":")

for i in range(2, numero + 1):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)

os.system("pause")