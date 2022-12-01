#include <iostream>
#include <string>
#include <random>
#include "carte.hpp"

int k = 0;
Carte tab[5];

int main()
{
    Carte carte1, carte2, carte3, carte4, carte5;
    tab[0] = carte1; tab[1] = carte2; tab[2] = carte3; tab[3] = carte4; tab[4] = carte5;
    while (k <= 5) {
        std::cout << tab[k].valeur[1] << " " << tab[k].couleur[1] << std::endl;
        k++;
    }
    k = 0;
}
