#include <iostream>
#include <random>
class Character {
public:
    Character(std::string name, int hp, int force, int defense) :
        name(name), hp(hp), force(force), defense(defense) {}

    virtual void attributes() {
        std::cout << name << ":" << std::endl;
        std::cout << "·Vida: " << hp << std::endl;
        std::cout << "·Daño: " << force << std::endl;
        std::cout << "·Defensa: " << defense << std::endl;
    }

    bool its_alive() {
        return hp > 0;
    }

    void die() {
        hp = 0;
        std::cout << name << " ha muerto" << std::endl;
    }

    int damage(Character& enemy) {
        return force - enemy.defense;
    }

    void attack(Character& enemy) {
        int damage = this->damage(enemy);
        enemy.hp = enemy.hp - damage;
        std::cout << name << " ha realizado " << damage << " puntos de daño a " << enemy.name << std::endl;
        if (enemy.its_alive()) {
            std::cout << "Vida de " << enemy.name << " es " << enemy.hp << std::endl;
        }
        else {
            enemy.die();
        }
    }

    bool dodge() {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<int> dis(1, 2);
        int aleatorio = dis(gen);
        if (aleatorio == 1) {
            std::cout << "Has esquivado la lanza de Odín" << std::endl;
            return true;
        }
        else {
            std::cout << "No has podido esquivar la embestida de Odín" << std::endl;
            return false;
        }
    }

public:
    std::string name;
    int hp;
    int force;
    int defense;
};

class Wizard : public Character {
public:
    Wizard(std::string name, int hp, int force, int defense, int wisdom) :
        Character(name, hp, force, defense), wisdom(wisdom) {}

    void attributes() {
        Character::attributes();
        std::cout << "·Sabiduría: " << wisdom << std::endl;
    }

    int damage(Character& enemy) {
        return force + wisdom - enemy.defense;
    }

public:
    int wisdom;
};

class Berserker : public Character {
public:
    Berserker(std::string name, int hp, int force, int defense, int fury) :
        Character(name, hp, force, defense), fury(fury) {}

    void attributes() {
        Character::attributes();
        std::cout << "·Furia: " << fury << std::endl;
    }

    int damage(Character& enemy) {
        return force + fury - enemy.defense;
    }

public:
    int fury;
};

class Assassin : public Character {
public:
    Assassin(std::string name, int hp, int force, int defense, int energy) :
        Character(name, hp, force, defense), energy(energy) {}

    void attributes() {
        Character::attributes();
        std::cout << "·Energía: " << energy << std::endl;
    }
    
    int damage(Character* enemy) {
        return force + energy - enemy->defense;
    }

public:
    int energy;
};

class Boss : public Character {
public:
    Boss(std::string name, int hp, int force, int defense) : 
        Character(name, hp, force, defense) {}
    
    void boss_attack(Character* enemy) {
    std::random_device rd;
    std::mt19937 rng(rd());
    std::uniform_int_distribution<int> uni(30, 60);
    auto damage = uni(rng);
    enemy->hp -= damage;
    std::cout << name << " ha realizado " << damage << " puntos de daño a "
              << enemy->name << std::endl;
    if (enemy->its_alive()) {
      std::cout << "Vida de " << enemy->name << " es " << enemy->hp
                << std::endl;
    } 
    else {
      enemy->die();
    }
  }
};

Character* choose_class() {
    std::cout << "Bienvenido al El Reino de Darthon. Elige tu clase:" << std::endl;
    std::cout << "1. Wizard" << std::endl;
    std::cout << "2. Berserker" << std::endl;
    std::cout << "3. Assassin" << std::endl;
    
    int choice;
    std::cin >> choice;
    
    std::string name;
    std::cout << "Escribe el nombre de tu personaje: ";
    std::cin >> name;
    
    if (choice == 1) {
        std::cout << "¡Bienvenido, " << name 
            << "! ¡Aprovecha tu sabiduría y magia para dezatar todo tu poder!" << std::endl;
        return new Wizard(name, 150, 30, 200, 350);
    } else if (choice == 2) {
            std::cout << "¡Bienvenido, " << name 
                << "! ¡Usa tu furia para aplastar a tus oponentes!" << std::endl;
            return new Berserker(name, 200, 40, 150, 250);
        } else if (choice == 3) {
                std::cout << "¡Bienvenido, " << name 
                    << "! ¡Utiliza tu astucia y sigilo para derrotar a tus victimas!" << std::endl;
                return new Assassin(name, 120, 35, 170, 300);
            }
};

std::string choose_action() {
    int contador = 0;
    while (true) {
        if (contador == 3) {
            std::cout << "Has superado el límite de intentos. Fin del juego." << std::endl;
            return "";
        }
        
        std::cout << "¿Qué quieres hacer?" << std::endl;
        std::cout << "1. Atacar" << std::endl;
        std::cout << "2. Esquivar" << std::endl;
        int option;
        std::cin >> option;
        
        if (option == 1) {
            return "atacar";
        } else if (option == 2) {
                return "esquivar";
            } else {
                std::cout << "Opción inválida" << std::endl;
                contador++;
            }
    }
};

void combat(Character* player, Boss* boss_1) {
    int round = 1;
    while (player->its_alive() && boss_1->its_alive()) {
        std::cout << "\nRonda " << round << std::endl;
        std::cout << ">>> Turno de " << player->name << " <<<" << std::endl;
        std::string act = choose_action();
        if (act == "atacar") {
            player->attack(boss_1);
            if (boss_1->its_alive()) {
                std::cout << ">>> Turno de " << boss_1->name << " <<<" << std::endl;
                boss_1->boss_attack(player);
            }
        } else if (act == "esquivar") {
                bool dodged = player->dodge();
                if (dodged) {
                    std::cout << "Odín retrocede" << std::endl;
                } else {
                    if (boss_1->its_alive()) {
                        std::cout << ">>> Turno de " << boss_1->name << " <<<" << std::endl;
                        boss_1->boss_attack(player);
                    }
                }
            }
        round++;
    }
    dodged = false;
};

Character* player = choose_class();
Boss boss_1("Odín", 400, 50, 250);

player->attributes();
boss_1.attributes();

combat(player, &boss_1);

if (!player->its_alive()) {
    std::cout << "\nHa ganado " << boss_1.name_ << std::endl;
} else if (!boss_1.its_alive()) {
        std::cout << "\nHa ganado " << player->name_ << std::endl;
    }
