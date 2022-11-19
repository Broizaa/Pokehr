#include <iostream>
#include <stdio.h>
#include <algorithm>

// AS = 14
// Roi = 13
// Dame = 12
// Valet = 11
// 10
// 9
// 8
// 7
// 6
// 5
// 4
// 3
// 2
// 1 = 14

using namespace std;

int array1[] = {10, 11, 12, 13, 14};
int array2[] = {3, 2, 4,9,15};
int suite[] = {2, 3, 4, 5, 6};
int QuinFLRO[] = {10, 11, 12, 13, 14};
int QuinFL[] = {8, 9, 10, 11, 12};



int affiche_tableau(int tab[], int borne_inf, int borne_sup)
{
    for(; borne_inf < borne_sup; borne_inf++)
    {
        std::cout << tab[borne_inf] << std::endl;
    }
    return 0;
}


int triBulle(int tab[], int size)
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
                affiche_tableau(array1, 0, 5 );
            }
        }
    }
}

int mostValue (int arr1[], int size){
    int max = 0;
    int val = 0;
    for (int i = 0; i < size; ++i) {
        val = arr1[i];
        if (val > max){
            max = val;
        }
    }
    std::cout << "La valeur Max est : " << max <<std::endl;
}

int mostFrequent(int* arr, int size){
    int maxcount = 0;
    int element_having_max_freq;
    for (int i = 0; i < size; i++) {
        int count = 0;

        for (int j = 0; j < size; j++) {
            if (arr[i] == arr[j])
                count++;
        }

        if (count > maxcount) {
            maxcount = count;
            element_having_max_freq = arr[i];
        }

    }

    std::cout << "le plus frequent : " << element_having_max_freq << std::endl;

    int count = 0;
    for (int i = 0; i < size; i++) {
        if (element_having_max_freq == arr[i]) {
            count++;
        }
    }

    std::cout << "Nombre de fois : " << count << std::endl;

    if (count == 2){
        std::cout << "PAIRE de " << element_having_max_freq <<std::endl;
        //faire fonction qui vérifie double pair ou full
    }
    if (count == 3){
        std::cout << "BRELAN de " << element_having_max_freq <<std::endl;
        // faire une vérification du full
    }
    if (count == 4){
        std::cout << "CARRE de " << element_having_max_freq <<std::endl;
    }
    if (count == 1){
        mostValue(array1, 5);
    }

}

int Suite (int arr1[], int arr2[]) {

    int m = sizeof(arr1) / sizeof(*arr1);
    int n = sizeof(arr2) / sizeof(*arr2);

    if (m == n && std::equal(arr1, arr1 + m, arr2)){
        std::cout << "suite" << std::endl;
    }
    else{
        std::cout << "pas une suite " << std::endl;
        mostFrequent(arr1, 5);
    }

}

int QtFl (int arr3[]) {

    int p = sizeof(arr3) / sizeof(*arr3);
    int q = sizeof(QuinFLRO) / sizeof(*QuinFL);

    if (p == q && std::equal(arr3, arr3 + p, QuinFL)){
        std::cout << "QUINTE FLUSH !!!" <<std::endl;
    }
    else{
        std::cout << "pas une Quinte Flush  " << std::endl;
        Suite(array1, suite);
    }

}


int QtFR (int arr2[]) {

    int s = sizeof(arr2) / sizeof(*arr2);
    int t = sizeof(QuinFLRO) / sizeof(*QuinFLRO);

    if (s == t && std::equal(arr2, arr2 + t, QuinFLRO)){
        std::cout <<" QUINTE FLUSH ROYAL !!!" << std::endl;
    }
    else{
        std::cout << "pas une Quinte Flush Royal " << std::endl;
        QtFl(array1);
    }

}



int main() {

    std::cout << "hello world" << std::endl;
    std::cout << "tableau de base" << std::endl;
    affiche_tableau(array1, 0, 5);
     std::cout << "Tableau trie" << std::endl;
    triBulle(array1, 5);
    //repet1(array, 5);
    //mostFrequent(array1, 5);
    QtFR(suite);
    return 0;

}



// PREMIERE FONCTION pour trouver la valeur la plus fréquente

/*
int repet1(int arr[], int size){
    int tabReponce[5]; //Tableau temporaire [valeur_max_du_tabValeur+1]
    int max=0; //valeur temporaire pour recuperer la plus grande valeur de tabReponce
    int valeurLaPlusFrequente=0; // valeur + de répétition

    for(int i=0;i<5;i++){ //mise a 0 du tableau reponce
        tabReponce[i]=0;
    }

    for (int i=0;i<sizeof(arr)/4;i++){//incrémentation de tabReponce en fonction de tabValeur[i]
        tabReponce[arr[i]]++;
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
   // std::cout<<"nb repetition : " << count <<std::endl;

 }
 */


//combinaison

/*
   if (count == 2){
       Paire(array, 5);
   }
   if (count == 3){
       std::cout << "BRELAN de " << valeurLaPlusFrequente <<std::endl;
   }
   if (count == 4){
       std::cout <<"CARRE !!!" << std::endl;
   }*/
