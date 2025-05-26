name = 'Lucas Felz'
experience = 0
number_of_kill_monsters = 0

while experience < 5001:
    experience += 10
    number_of_kill_monsters += 1
    print(f"{name} matou um monstro. XP atual: {experience}")

if experience >= 5001:
    print(f"{name} alcançou o ranking ouro ultrapassando 5001 de XP alcançada!\n")
