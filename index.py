#Entrada
nome = input("Digite o nome do seu herói: ").title()
xp = int(input("Digite a quantidade de XP do seu herói: "))

#Lista de níveis com seus nomes e limites 
niveis = [
    (10001, "Radiante"),
    (9001, "Imortal"),
    (8001, "Ascendente"),
    (7001, "Platina"),
    (5001, "Ouro"),
    (2001, "Prata"),
    (1001, "Bronze"),
    (0, "Ferro")
]

#Laço para encontrar o nível correspondente ao XP
for limite, nivel in niveis:
    if xp >= limite:
        break

#Saída
print(f"O Herói {nome} está no nível de {nivel}")