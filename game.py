import random
class Character:
    def __init__(self, name, hp=1000, damage=200, defense=300, magic=100):
        self.__name = name
        self.__hp = hp
        self.__damage = damage
        self.__defense = defense
        self.__magic = magic
    
    def set_name(self, name):                           #sets and gets
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_hp(self, hp):
        self.__hp = hp
    
    def get_hp(self):
        return self.__hp

    def set_damage(self, damage):
        self.__damage = damage
    
    def get_damage(self):
        return self.__damage
    
    def set_defense(self, defense):
        self.__defense = defense
    
    def get_defense(self):
        return self.__defense
    
    def set_magic(self, magic):
        self.__magic = magic
    
    def get_magic(self):
        return self.__magic
    
class Wizard(Character):
    def __init__(self,name,hp=1000,damage=200,defense=300,magic=100,wisdom=500):
        super().__init__(name,hp=1300,damage=100,defense=200,magic=600)
        self.__wisdom = wisdom

    def set_wisdom(self, wisdom):
        self.__wisdom = wisdom
    
    def get_wisdom(self):
        return self.__wisdom

    def attack(self):               
        r = random.uniform(200, self.__wisdom)
        return r

class Berserker(Character):
    def __init__(self,name,hp=1000,damage=200,defense=300,magic=100,fury=500):
        super().__init__(name,hp=2000,damage=350,defense=400,magic=10)
        self.__fury = fury

    def set_fury(self, fury):
        self.__fury = fury
    
    def get_fury(self):
        return self.__fury

    def attack(self):               
        r = random.uniform(200, self.__fury)
        return r

class Assassin(Character):
    def __init__(self,name,hp=1000,damage=200,defense=300,magic=100,energy=500):
        super().__init__(name,hp=1600,damage=450,defense=200,magic=50)
        self.__energy = energy

    def set_energy(self, energy):
        self.__energy = energy
    
    def get_magic(self):
        return self.__energy

    def attack(self):               
        r = random.uniform(200, self.__energy)
        return r

class Boss(Character):
    def __init__(self,name,hp=1000, damage=500):
        super().__init__(name,hp=hp, damage=damage)
        self.__hp = hp
        self.__damage = random.uniform(500, 600)
    
    def set_hp(self, hp):
        self.__damage = hp
    
    def get_hp(self):
        return self.__hp

    def set_damage(self, damage):
        self.__damage = damage
    
    def get_damage(self):
        return self.__damage
    
    def attack(self):
        return self.__damage

def choose_class():
    print("Bienvenido al El Reino de Darthon. Elige tu clase:")
    print("1. Wizard")
    print("2. Berserker")
    print("3. Assassin")
    
    choice = int(input("Escribe el número de la clase que quieres elegir: "))
    
    name = input("Escribe el nombre de tu personaje: ")

    if choice == 1:
        print(f"¡Bienvenido, {name}! ¡Aprovecha tu sabiduría y magia para derrotar al jefe!")
        return Wizard(name)
    elif choice == 2:
        print(f"¡Bienvenido, {name}! ¡Usa tu furia para aplastar al jefe!")
        return Berserker(name)
    elif choice == 3:
        print(f"¡Bienvenido, {name}! ¡Utiliza tu astucia y sigilo para derrotar al jefe!")
        return Assassin(name)

character = choose_class()
print("Comienzas explorar un bosque en busqueda de unos niños perdidos que jugaban por aquí...")
print(f"De repente se te hacerca un mounstruo con gran velocidad y apenas logras esquivarlo, ¿Qué harás ahora {character.get_name()}?")

boss = Boss("THOR", hp=1000, damage=500) # boss 1 es rapido(ataca primero) tiene daño 

def combat(character, boss):
    while character.get_hp() > 0 and boss.get_hp() > 0:
        print("Es tu turno. Elige una opción:")
        print("1. Atacar")
        print("2. Esquivar")
        print("3. Defenderse")
        choice = int(input())   
        if choice == 1:
            damage = character.attack()
            boss.set_hp(boss.get_hp() - damage)
            print(f"Le has hecho {damage} de daño al jefe.")
        elif choice == 2:
            rand = random.uniform(0, 1)
            # Si el número es menor o igual a 0.5, logró esquivar el ataque
            if rand <= 0.5:
                print("¡Has logrado esquivar el ataque del jefe!")
            # Si el número es mayor a 0.5, no logró esquivar el ataque y recibe daño normalmente
            else:
                damage = boss.attack()
                character.set_hp(character.get_hp() - damage)
                print(f"El jefe te ha hecho {damage} de daño.")         # 1/2 de probabilidad
        elif choice == 3:
            character.set_defense(character.get_defense() + 100)
        
        damage = boss.attack()
        if choice == 3:
            damage -= character.get_defense()
            character.set_defense(character.get_defense() - 100)
        character.set_hp(character.get_hp() - damage)
        print(f"El jefe te ha hecho {damage} de daño.")
    
    if character.get_hp() <= 0:
        print("Has perdido el combate.")
    else:
        print("¡Felicidades, has ganado el combate!")
combat(character, boss)

boss2 = Boss("LOKI", hp=1000, damage=500) # boss 2 mucha vida, mucho daño, poca probabilidad de pegar # 1/4 de probabilidad

boss3 = Boss("ODIN", hp=1000, damage=1000) # se demora 3 turnos en pegar, 2/3 de probabilidad de pegar 
