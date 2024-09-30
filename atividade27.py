# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria

lista = []

for i in range(7):
    convidados = str(input(f"Digite o Nome do Convidado{i+1}:"))
    lista.append(convidados)

rmv = str(input("deseja remover algum Convidado?(sim/não)"))
if rmv == 'sim':
    nome = str(input("Qual convidado:"))
    lista.remove(nome)
    print(lista)
    
elif rmv == 'não':
    print("Ok")