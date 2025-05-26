


def main(name, experience, number_of_kill_monsters):
    experience += 10
    number_of_kill_monsters += 1
    print(f"{name} matou um monstro. XP atual: {experience}")
    return experience, number_of_kill_monsters

name = 'Lucas Felz'
experience = 0
number_of_kill_monsters = 0

while experience < 5001:
    experience, number_of_kill_monsters = main(name, experience, number_of_kill_monsters)


print(f"{name} alcançou o ranking ouro ultrapassando 5001 de XP alcançada!\n")