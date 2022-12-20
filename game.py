import random
#numero_aleatorio = random.randint(1, 10) #para obtener un número entero aleatorio entre 1 y 10, puedes utilizar la función randint
#función random() para obtener un número aleatorio entre 0 y 1
#función uniform(a, b) para obtener un número aleatorio flotante entre a y b
class Character:
    def __init__(self,hp=1000,attack=200,defense=300,magic=100):
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._magic = magic

    def welcome(self):
        print("Bienvenido jugador selecciona un pj")

    def set_hp(self, hp):                           #sets and gets
        self.__hp = hp
    
    def get_hp(self):
        return self.__hp

    def set_attck(self, attack):
        self.__attack = attack
    
    def get_attack(self):
        return self.__attack
    
    def set_defense(self, defense):
        self.__defense = defense
    
    def get_defense(self):
        return self.__defense
    
    def set_magic(self, magic):
        self.__magic = magic
    
    def get_magic(self):
        return self.__magic
    
class Wizard(Character):
    def __init__(self,hp=1000,attack=200,defense=300,magic=100,wisdom=500):
        super().__init__(hp=1300,attack=100,defense=200,magic=600)
        self._wisdom = wisdom

class Berserker(Character):
    def __init__(self,hp=1000,attack=200,defense=300,magic=100,fury=500):
        super().__init__(hp=2000,attack=350,defense=400,magic=10)
        self._fury = fury

class Assassin(Character):
    def __init__(self,hp=1000,attack=200,defense=300,magic=100,energy=500):
        super().__init__(hp=1600,attack=450,defense=200,magic=50)
        self._energy = energy
