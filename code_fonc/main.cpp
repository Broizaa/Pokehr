#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <random>



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

// trèfle = 20
// coeur = 21
// pique = 22
// carreaux = 23


using namespace std;

//main 1
int tab1[] = {11, 3, 11, 3, 5};
int coul1[] = {20, 20, 20, 20,22};

//main 2
int tab2[] = {4, 2, 4, 5, 2};
int coul2[] = {22,22,22,20,22};

//tableau de comparaison
int QuinFLRO[] = {10, 11, 12, 13, 14};
int QuinFL[] = {8, 9, 10, 11, 12};
int trefle[] = {20, 20, 20, 20,20};
int coeur[] = {21, 21, 21, 21, 21};
int pique[] = {22, 22, 22, 22, 22};
int carro[] = {23, 23, 23, 23, 23};


int force;


// fonction qui permet d'afficher un tableau

int affiche_tableau(int tab[], int borne_inf, int borne_sup)
{
    for(; borne_inf < borne_sup; borne_inf++)
    {
        std::cout << tab[borne_inf] << std::endl;
    }
    return 0;
}

// Fonction qui permet de faire un tri croissant du tableau
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

// Fonction qui permet de cherche la valeur la plus élevé.

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


// Fonction qui permet de trouver la valeur qui se repète le plus
int mostFrequent(int* arr, int size){
    // cherche la valeur
    int maxcount = 0;
    int valeur_repet;
    for (int i = 0; i < size; i++) {
        int count = 0;

        for (int j = 0; j < size; j++) {
            if (arr[i] == arr[j])
                count++;
        }

        if (count > maxcount) {
            maxcount = count;
            valeur_repet = arr[i];
        }

    }

    std::cout << "le plus frequent : " << valeur_repet << std::endl;

    // compte le nombre de répétition
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (valeur_repet == arr[i]) {
            count++;
        }
    }

    std::cout << "Nombre de fois : " << count << std::endl;

    if (count == 2){
        //recherche de la double paire
        if ( arr[0] == arr[1] && arr[0]!= valeur_repet || arr[2] == arr[3] && arr[2] != valeur_repet || arr[3] == arr[4] && arr[3] != valeur_repet){
            std::cout << "Double paire" << std::endl;
            force =3;
            std::cout << "La force est de " << force << std::endl;
        }
        else{
            std::cout << "PAIRE de " << valeur_repet <<std::endl;
            force = 2;
            std::cout << "La force est de " << force << std::endl;
        }


    }
    if (count == 3){
        //recherche du full
        if ( arr[0] == arr[1] && arr[0]!= valeur_repet || arr[3] == arr[4] && arr[3] != valeur_repet){
            std::cout << "full" << std::endl;
            force = 8;
            std::cout << "La force est de " << force << std::endl;
        }
        else{
            std::cout << "Brelan " << valeur_repet <<std::endl;
            force = 4;
            std::cout << "La force est de " << force << std::endl;
        }
    }
    if (count == 4){
        std::cout << "CARRE de " << valeur_repet <<std::endl;
        force = 8;
        std::cout << "La force est de " << force << std::endl;
    }
    if (count == 1){
        mostValue(arr, 5);
    }

}

/*
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

}*/

// Fonction qui permet de savoir si c'est une suite

int Suite(int arr1[]){
    int i=0;
    if( arr1[i]== arr1[i+1]-1 && arr1[i+1]-1== arr1[i+2]-2 && arr1[i+2]-2== arr1[i+3]-3 && arr1[i+3]-3== arr1[i+4]-4){
        std::cout << "suite" << std::endl;
        force=5;
        std::cout << "la force est de "<< force << std::endl;
    }
    else{
        std::cout << "pas de suite" << std::endl;
        mostFrequent(arr1,5);
    }
}

// Fonction qui permet de savoir si c'est une couleur

int couleur(int cou7[], int arr7[]){
    int a = 5;
    if (std::equal(cou7, cou7 + a, coeur)){
        std::cout << "couleur de coeur" << std::endl;
        force = 6;
        std::cout << "La force est de " << force << std::endl;
    }
    if (std::equal(cou7, cou7 + a, trefle)){
        std::cout << "couleur de trefle" << std::endl;
        force = 6;
        std::cout << "La force est de " << force << std::endl;
    }
    if (std::equal(cou7, cou7 + a, carro)){
        std::cout << "couleur de carreaux" << std::endl;
        force = 6;
        std::cout << "La force est de " << force << std::endl;
    }
    if (std::equal(cou7, cou7 + a, pique)){
        std::cout << "couleur de pique" << std::endl;
        force = 6;
        std::cout << "La force est de " << force << std::endl;
    }
    else{
        Suite(arr7);
    }

}

// Fonction qui permet de savoir si c'est une quinte flush

int QtFl (int arr3[], int cou2[]) {

    int p = 5;
    int q = 5;

    if (p == q && std::equal(arr3, arr3 + p, QuinFL)){
        if (cou2[0] == cou2[1] && cou2[1] == cou2[2] && cou2[2] == cou2[3] && cou2[3] == cou2[4]){
            std::cout << "QUINTE FLUSH !!!" <<std::endl;
            force = 9;
            std::cout << "La force est de " << force << std::endl;
        }
        else{
            std::cout << "pas une Quinte Flush  " << std::endl;
            Suite(arr3);
        }

    }
    else{
        std::cout << "pas une Quinte Flush  " << std::endl;
        Suite(arr3);
    }

}

// Fonction qui permet de savoir si c'est une quinte flush royal

int QtFR (int arr2[], int cou1[]) {
    force = 0;
    int s = 5;
    int t = 5;
    if (s == t && std::equal(arr2, arr2 + t, QuinFLRO) ){
        if (cou1[0] == cou1[1] && cou1[1] == cou1[2] && cou1[2] == cou1[3] && cou1[3] == cou1[4]){
            std::cout <<" QUINTE FLUSH ROYAL !!!" << std::endl;
            force = 10;
            std::cout << "La force est de " << force << std::endl;
        }
        else{
            std::cout << "pas une Quinte Flush Royal " << std::endl;
            QtFl(arr2, cou1);
        }

    }
    else{
        std::cout << "pas une Quinte Flush Royal " << std::endl;
        couleur(cou1, arr2);
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

    triBulle(tab1, 5);
    QtFR(tab1, coul1 );

    main1 = force;
    std::cout << "La force de la main 1 est de "<< main1 << std::endl;


    std::cout<<"MAIN 2" <<std::endl;

    triBulle(tab2, 5);
    QtFR(tab2, coul2 );

    main2 = force;
    std::cout <<"la force de la main 2 est de "<< main2 << std::endl;


    std::cout <<"Qui gagne ?"<<std::endl;
    if (main1 > main2){
        std::cout << "Le combinaison la plus forte est la main 1" <<std::endl;
    }
    if (main1 < main2){
        std::cout << "Le combinaison la plus forte est la main 2" <<std::endl;
    }
    if (main1 == main2){
        std::cout << "Les combinaisons des deux mains sont egales" <<std::endl;
    }


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
