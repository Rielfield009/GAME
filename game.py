import random
class Character:
    def __init__(self, name, hp, force, defense):
        self.name = name
        self.hp = hp
        self.force = force
        self.defense = defense
        
    def attributes(self):
        print(self.name, ":", sep="")
        print("·Vida:", self.hp)
        print("·Daño:", self.force)
        print("·Defensa:", self.defense)

    def its_alive(self):
        return self.hp > 0

    def die(self):
        self.hp = 0
        print(self.name, "ha muerto")

    def damage(self, enemy):
        return self.force - enemy.defense
    
    def attack(self, enemy):
        damage = self.damage(enemy)
        enemy.hp = enemy.hp - damage
        print(self.name, "ha realizado", damage, "puntos de daño a", enemy.name)
        if enemy.its_alive():
            print("Vida de", enemy.name, "es", enemy.hp)
        else:
            enemy.die()

    def dodge(self, enemy):
        aleatorio = random.randint(1, 2)
        if aleatorio == 1:
            print("Has esquivado el ataque del enemigo")
        else:
            enemy.attack(self)
        
class Wizard(Character):
    def __init__(self, name, hp, force, defense, wisdom):
        super().__init__(name, hp, force, defense)
        self.wisdom = wisdom
    
    def attributes(self):
        super().attributes()
        print("·Sabiduría:", self.wisdom)

    def damage(self, enemy):
        return self.force*self.wisdom - enemy.defense
              
class Berserker(Character):
    def __init__(self,name,hp, force, defense, fury):
        super().__init__(name, hp, force, defense)
        self.fury = fury

    def attributes(self):
        super().attributes()
        print("·Furia:", self.fury)
    
    def damage(self, enemy):
        return self.force*self.fury - enemy.defense
              
class Assassin(Character):
    def __init__(self,name, hp, force, defense, energy):
        super().__init__(name, hp, force, defense)
        self.energy = energy

    def attributes(self):
        super().attributes()
        print("·Energía:", self.energy)

    def damage(self, enemy):
        return self.force*self.energy - enemy.defense
              
class Boss(Character):
    def __init__(self,name, hp, force, defense):
        super().__init__(name, hp, force, defense)
    
    def damage(self, enemy):
        return self.force*self.hp - enemy.defense

def choose_class():
    print("Bienvenido al El Reino de Darthon. Elige tu clase:")
    print("1. Wizard")
    print("2. Berserker")
    print("3. Assassin")
    
    choice = int(input("Escribe el número de la clase que quieres elegir: "))
    
    name = input("Escribe el nombre de tu personaje: ")

    if choice == 1:
        print(f"¡Bienvenido, {name}! ¡Aprovecha tu sabiduría y magia para dezatar todo tu poder!")
        return Wizard(name, 100, 30, 200, 350)
    elif choice == 2:
        print(f"¡Bienvenido, {name}! ¡Usa tu furia para aplastar a tus oponentes!")
        return Berserker(name, 100, 30, 200, 350)
    elif choice == 3:
        print(f"¡Bienvenido, {name}! ¡Utiliza tu astucia y sigilo para derrotar a tus victimas!")
        return Assassin(name, 100, 30, 200, 350)

def choose_action():
        contador = 0
        while True:
            if contador == 3:
                print("Has superado el límite de intentos. Fin del juego.")
                return

            print("¿Qué quieres hacer?")
            print("1. Atacar")
            print("2. Esquivar")
            option = int(input())

            if option == 1:
                return "atacar"
            elif option == 2:
                return "esquivar"
            else:
                print("Opción inválida")
                contador += 1
    
def combat(player, boss_1):
  turno = 0
  while player.its_alive() and boss_1.its_alive():
    if player.hp <= 0:
      print("\nHa ganado", boss_1.name)
      break
    if boss_1.hp <= 0:
      print("\nHa ganado", player.name)
      break

    print("\nTurno", turno)
    print(">>> Acción de ", player.name,":", sep="")
    act = choose_action()
    if act == "atacar":
      player.attack(boss_1)
    elif act == "esquivar":
      dodged = player.dodge(boss_1)
      if dodged:
        print("El ataque del jefe ha sido esquivado")
        continue
    else:
      print("Acción inválida")
      continue
    print(">>> Acción de ", boss_1.name,":", sep="")
    if not dodged:
        boss_1.attack(player)
    turno = turno + 1

player = choose_class()
boss_1 = Boss("Odin", 100, 500, 100)

player.attributes()
boss_1.attributes()

combat(player, boss_1)
