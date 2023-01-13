#include <iostream>
#include "game.h"

using namespace std;

int main() {
    Character* player = choose_class();
    Boss boss_1("Odín", 350, 50, 250);

    player->attributes();
    boss_1.attributes();

    combat(player, &boss_1);

    if (!player->its_alive()) {
        cout << "\nHa ganado " << boss_1.name << endl;
    } else if (!boss_1.its_alive()) {
        cout << "\nHa ganado " << player->name << endl;
        cout << "\nFelicidades, FIN." << endl;
        cout << "CREDITOS:" << endl;
        cout << "Jose Peña" << endl << "Jean Moscoso" << endl << "Giovanni González" << endl;
        delete player;
        }
    return 0;
}
