import random
#numero_aleatorio = random.randint(1, 10) #para obtener un número entero aleatorio entre 1 y 10, puedes utilizar la función randint
#función random() para obtener un número aleatorio entre 0 y 1
#función uniform(a, b) para obtener un número aleatorio flotante entre a y b
class Character:
    def __init__(self,hp=1000,damage=200,defense=300,magic=100):
        self.__hp = hp
        self.__damage = damage
        self.__defense = defense
        self.__magic = magic

    def set_hp(self, hp):                           #sets and gets
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
    def __init__(self,hp=1000,damage=200,defense=300,magic=100,wisdom=500):
        super().__init__(hp=1300,damage=100,defense=200,magic=600)
        self.__wisdom = wisdom

    def set_wisdom(self, wisdom):
        self.__wisdom = wisdom
    
    def get_wisdom(self):
        return self.__wisdom

    def attack(self):               #call of darkness
        r = random.uniform(200, self.__wisdom)
        return r

class Berserker(Character):
    def __init__(self,hp=1000,damage=200,defense=300,magic=100,fury=500):
        super().__init__(hp=2000,damage=350,defense=400,magic=10)
        self.__fury = fury

    def set_fury(self, fury):
        self.__fury = fury
    
    def get_fury(self):
        return self.__fury

    def attack(self):               #fury unleashed
        r = random.uniform(200, self.__fury)
        return r

class Assassin(Character):
    def __init__(self,hp=1000,damage=200,defense=300,magic=100,energy=500):
        super().__init__(hp=1600,damage=450,defense=200,magic=50)
        self.__energy = energy

    def set_energy(self, energy):
        self.__energy = energy
    
    def get_magic(self):
        return self.__energy

    def attack(self):               #fury unleashed
        r = random.uniform(200, self.__energy)
        return r

class Boss(Character):
    def __init__(self, hp=1000, damage=500):
        super().__init__(hp=hp, damage=damage)
        self.__damage = random.uniform(500, 600)
    
    def attack(self):
        return self.__damage

boss1 = Boss()
boss2 = Boss()
def choose_class():
    print("Bienvenido al El Reino de Darthon. Elige tu clase:")
    print("1. Wizard")
    print("2. Berserker")
    print("3. Assassin")
    
    # Obtener la opción elegida por el usuario
    choice = int(input("Escribe el número de la clase que quieres elegir: "))
    
    # Crear una instancia de la clase elegida y retornarla
    if choice == 1:
        return Wizard()
    elif choice == 2:
        return Berserker()
    elif choice == 3:
        return Assassin()
