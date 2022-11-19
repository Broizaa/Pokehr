#include <iostream>
#include <stdio.h>

using namespace std;

int array [] = {9, 3, 9,5,3};
int array2[] = {3, 2, 4,9,15};
int suite[] = {2, 3, 4, 5, 6};

int affiche_tableau(int tab[], int borne_inf, int borne_sup)
{
    for(; borne_inf < borne_sup; borne_inf++)
    {
        std::cout << tab[borne_inf] << std::endl;
    }
    return 0;
}

int tribulle(int tab[], int size)
{
    int i, j;
    int temp;
    for(i=0; i<size; i++){
        for (j=i +1; j<size; j++)
        {
            if (tab[i] > tab[j]){
                temp = tab[i];
                tab[i] = tab[j];
                tab[j] = temp;
                std::cout << "new tableau" << std::endl;
                affiche_tableau(array, 0, 5 );
            }
        }
    }
}



int test_suite()
{

}

int repet1(int arr[], int size){
    int tabReponce[5]; //Tableau temporaire [valeur_max_du_tabValeur+1]
    int max=0; //valeur temporaire pour recuperer la plus grande valeur de tabReponce
    int valeurLaPlusFrequente=0; // valeur + de répétition

    for(int i=0;i<5;i++){ //mise a 0 du tableau reponce
        tabReponce[i]=0;
    }

    for (int i=0;i<sizeof(array)/4;i++){//incrémentation de tabReponce en fonction de tabValeur[i]
        tabReponce[array[i]]++;
    }

    for (int i=0;i<5;i++){//recuperation de la valeur la plus frequente
        if(tabReponce[i]>max){
            max=tabReponce[i];
            valeurLaPlusFrequente=i;
        }
    }
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (valeurLaPlusFrequente == arr[i]) {
            count++;
        }
    }

    cout<<"Valeur La Plus Frequente : " << valeurLaPlusFrequente<<endl;
    std::cout<<"nb repetition : " << count <<std::endl;



    //combinaison

    if (count == 2){
        std::cout << "PAIRE !!!" << std::endl;
    }
    if (count == 3){
        std::cout << "BRELAN !!!" <<std::endl;
    }
    if (count == 4){
        std::cout <<"CARRE !!!" << std::endl;
    }
}
/*
repet2(int arr[], int size){
    int tabReponce[5]; //Tableau temporaire [valeur_max_du_tabValeur+1]
    int max=0; //valeur temporaire pour recuperer la plus grande valeur de tabReponce
    int valeurLaPlusFrequente=0; // valeur + de répétition
    int recherche = 0; // variable de stockage


};

*/
int main() {
    std::cout << "hello world" << std::endl;
    std::cout << "tableau de base" << std::endl;
    affiche_tableau(array, 0, 5);
    tribulle(array, 5);
    repet1(array, 5);
    std::cout << "nombre de repetition" << std::endl;
   // frequency_count(array, 2, 5);
    return 0;
}


