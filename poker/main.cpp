#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <random>
#include "Carte.h"


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

//main
int array1[] = {9, 10, 11, 12, 13};
int array2[] = {14, 13, 10,12,11};

//tableau de comparaison
int suite[] = {2, 3, 4, 5, 6};
int QuinFLRO[] = {10, 11, 12, 13, 14};
int QuinFL[] = {8, 9, 10, 11, 12};
int force;



int affiche_tableau(int tab[], int borne_inf, int borne_sup)
{
    for(; borne_inf < borne_sup; borne_inf++)
    {
        std::cout << tab[borne_inf] << std::endl;
    }
    return 0;
}


int* triBulle(int arr6[], int size)
{
    int i, j;
    int temp;
    for(i=0; i<size; i++){
        for (j=i +1; j<size; j++)
        {
            if (arr6[i] > arr6[j]){
                temp = arr6[i];
                arr6[i] = arr6[j];
                arr6[j] = temp;
                //std::cout << "new tableau" << std::endl;
                //affiche_tableau(arr6, 0, 5 );
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
    force = 1;
    std::cout << "La force est de " << force << std::endl;
}

int FuLL(){
    std::cout << "full" <<std::endl;
}

int DoublePaire(){
    std::cout << "Double Paire" <<std::endl;
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
        //DoublePaire();
        force = 2;
        std::cout << "La force est de" << force << std::endl;
        //faire fonction qui vérifie double pair ou full
    }
    if (count == 3){
        std::cout << "BRELAN de " << element_having_max_freq <<std::endl;
        // faire une vérification du full
        force = 4;
        std::cout << "La force est de " << force << std::endl;
        //FuLL();
    }
    if (count == 4){
        std::cout << "CARRE de " << element_having_max_freq <<std::endl;
        force = 8;
        std::cout << "La force est de " << force << std::endl;
    }
    if (count == 1){
        mostValue(arr, 5);
    }

}

int Suite (int arr1[]) {

    int m = 5;
    int n = 5;

    if (m == n && std::equal(arr1, arr1 + m, suite)){
        std::cout << "suite" << std::endl;
        force = 5;
        std::cout << "La force est de " << force << std::endl;
    }
    else{
        std::cout << "pas une suite " << std::endl;
        mostFrequent(arr1, 5);
    }

}

int Suite2(int arr1[]){
    int i=0;
    if(std::equal(arr1[i], arr1[i+1]-1, arr1[i+2]-2, arr1[i+3]-3==arr1[i+4]-4){
        std::cout << 'suite' << std::endl;
        force=5;
        std::cout << 'la force est de' << force << std::endl;
    }
    else{
        std::cout << 'pas de suite' << std::endl;
        mostFrequent(arr1,5);
    }
}

int QtFl (int arr3[]) {

    int p = 5;
    int q = 5;

    if (p == q && std::equal(arr3, arr3 + p, QuinFL)){
        std::cout << "QUINTE FLUSH !!!" <<std::endl;
        force = 9;
        std::cout << "La force est de " << force << std::endl;
    }
    else{
        std::cout << "pas une Quinte Flush  " << std::endl;
        Suite2(arr3);
    }

}


int QtFR (int arr2[]) {
    force = 0;
    int s = 5;
    int t = 5;

    if (s == t && std::equal(arr2, arr2 + t, QuinFLRO)){
        std::cout <<" QUINTE FLUSH ROYAL !!!" << std::endl;
        force = 10;
        std::cout << "La force est de " << force << std::endl;
    }
    else{
        std::cout << "pas une Quinte Flush Royal " << std::endl;
        QtFl(arr2);
    }

}



int main() {
    int main1 = 0;
    int main2 = 0;
    std::cout << "hello world" << std::endl;
    //std::cout << "tableau de base" << std::endl;
    //affiche_tableau(array1, 0, 5);
    //std::cout << "Tableau trie" << std::endl;
    std::cout<<"MAIN 1" <<std::endl;

    triBulle(array1, 5);
    Suite2(array1);
    //repet1(array, 5);
    //mostFrequent(array1, 5);
    /*
    QtFR(array1);
    main1 = force;
    std::cout << "La force de la main 1 est de "<< main1 << std::endl;
    std::cout<<"MAIN 2" <<std::endl;
    triBulle(array2, 5);
    QtFR(array2);
    main2 = force;
    std::cout <<"Qui gagne ?"<<std::endl;
    std::cout <<"la force de la main 2 est de "<< main2 << std::endl;
    if (main1 > main2){
        std::cout << "Le combinaison la plus forte est la main 1" <<std::endl;
    }
    if (main1 < main2){
        std::cout << "Le combinaison la plus forte est la main 2" <<std::endl;
    }
    if (main1 = main2){
        std::cout << "Les combinaisons des deux mains sont égales" <<std::endl;
    }
*/
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
