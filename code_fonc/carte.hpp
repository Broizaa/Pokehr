 #ifndef DEF_CARTE
#define DEF_CARTE

#include <iostream>

class Carte
{
    public:
    Carte();                    //constructor
    ~Carte();                   //destructor
    
    //private:
    std::string couleur[];
    std::string valeur[];
};

#endif
