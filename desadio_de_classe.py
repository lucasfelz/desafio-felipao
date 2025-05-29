class Hero:

    def __init__(self, name, age, type):
        # Da início as propriedades da classe hero com nome, idade e tipo
        self.name = name
        self.age = age
        self.type = type
        

    def attack(self):
        if self.type == "mago":
            print(f"O {self.type}, chamado {self.name}, de {self.age} anos de idade, está pronto para a batalha:")
            print(f"O {self.type} usou magia")

        if self.type == "guerreiro":
            print(f"O {self.type}, chamado {self.name}, de {self.age} anos de idade, está pronto para a batalha:")
            print(f"O {self.type} usou espada")

        if self.type =="monge":
            print(f"O {self.type}, chamado {self.name}, de {self.age} anos de idade, está pronto para a batalha:")
            print(f"O {self.type}  usou artes marciais")

        if self.type == "ninja":
            print(f"O {self.type}, chamado {self.name}, de {self.age} anos de idade, está pronto para a batalha:")
            print(f"O {self.type} usou shuriken")


my_hero = Hero('Lucas', '28', 'ninja')
my_hero.attack()

