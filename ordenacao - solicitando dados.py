import os
os.system("cls || clear")

lista_nomes = []

#Entrada
print("=== Solicitando dados para o usuário")
while True:
    nome = input("Digite um nome: ")
    if nome.lower() == "sair":
        break
    else:
        lista_nomes.append(nome)

#Processamento
print("\nOrdenando lista...")
lista_ordenada = sorted(lista_nomes)

#Saída
print("\n === Resultado ===")
print(f"Lista original: ")
print(lista_nomes)

print("\n Lista ordenada:")
print(lista_ordenada)