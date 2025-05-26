class Hero:
    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.number_of_kill_monsters = 0

    def kill_monsters(self):
        self.experience += 10
        self.number_of_kill_monsters += 1
        print(f"{self.name} matou um monstro. XP atual: {self.experience}")

    def exibir_info_heroi(self):
        print(f"Heroi: {self.name}")
        print(f"Experiência: {self.experience}")
        print(f"Monstros derrotados: {self.number_of_kill_monsters}")

def main():
    hero1 = Hero('Lucas Felz')
    
    while hero1.experience < 5001:
        hero1.kill_monsters()


    print(f"{hero1.name} alcançou o ranking ouro ultrapassando 5001 de XP alcançada!\n")
    hero1.exibir_info_heroi()

    

if __name__ == '__main__':
    main()