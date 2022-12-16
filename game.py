class Character:
    def __init__(self,hp=1000,attack=200,defense=300,magic=100):
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._magic = magic

    def welcome(self):
        print("Bienvenido jugador selecciona un pj")
    
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
