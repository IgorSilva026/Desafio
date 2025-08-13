#Entrada
nome = input("Digite o nome do seu herói: ").title()
xp = int(input("Digite a quantidade de XP do seu herói: "))
vitorias = int(input("Digite quantas vitorias voce tem: "))
derrotas = int(input("digite quantas derrotas voce tem: "))

#Calcular o saldo de vitorias
saldo_vitorias = vitorias - derrotas

#Lista de níveis com seus nomes e limites 
niveis = [
    (10001, "Divino"),
    (9001, "Épico"),
    (8001, "Lenda"),
    (7001, "Mestre"),
    (5001, "Campeão"),
    (2001, "Veterano"),
    (1001, "Guerreiro"),
    (0, "Aprendiz")
]

#Lista de rank com nomes e qunatidades de vitoria
ranks = [
    (101, "Imortal"),
    (91, "Lendario"),
    (81, "Diamante"),
    (51, "Ouro"),
    (21, "Prata"),
    (11, "Bronze"),
    (0, "Ferro")
]

#Laço para encontrar o nível correspondente ao XP
for limite, nivel in niveis:
    if xp >= limite:
        nivel_heroi = nivel
        break
    
#laço para encontrar o rank 
for limite, nome_rank in ranks:
    if vitorias >= limite:
        rank_heroi = nome_rank
        break
    
#Saída
print(f"O Herói {nome} está no nível {nivel_heroi}, no rank {rank_heroi} e o seu saldo de vitorias é: {saldo_vitorias}")
