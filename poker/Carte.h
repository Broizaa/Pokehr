#ifndef DEF_CARTE
#define DEF_CARTE

#include <iostream>

using namespace std;

class Carte
{
public:
    Carte();                    //constructor
    ~Carte();                   //destructor

private:
    std::string m_couleur;
    int m_valeur;
};

#endif
