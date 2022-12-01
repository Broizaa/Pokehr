//
// Created by Clément Szewczyk on 28/10/2022.
//
#include <iostream>
#include <vector>
#include "Carte.h"

/*
int Rand( int a, int b)
{
    int nRand ;
    nRand= a + (int)((float)rand() * (b-a+1) / (RAND_MAX-1)) ;
    return nRand;
}

Carte* card(){
    char C ;
    char K ;
    char P ;
    char T ;

    char couleur[4] = {'C', 'K', 'P', 'T'};
    int valeur[13] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14};

    Carte* carte1 = new Carte;

    Rand(0,10);
    carte1->setCou(couleur[Rand(0,3)]);
    carte1->setVal(valeur[Rand(0,12)]);

    std::cout << "la couleur est : " << carte1.val << std::endl;
    std::cout << "la couleur est : " << carte1.cou << std::endl;

    return carte1;
}

std::vector<Carte*> paquet;
Carte* main1[5]={};



int jeu1(){
    srand(time(NULL));

    paquet.push_back(card());
    paquet.push_back(card());
    paquet.push_back(card());
    paquet.push_back(card());
    paquet.push_back(card());
    std::cout << "main 1" << std::endl;
    for (int i=0; i < 6; i++)
    {
        //main1[i] = card();
        int aleatoire = Rand(0, paquet.size() - 1);
        main1[i] = paquet[aleatoire];
        paquet.erase(paquet.begin() + aleatoire);
        std::cout << "carte" << i+1 <<std::endl;
        std::cout << main1[i]->getVal() << std::endl;
        std::cout << main1[i]->getCou() << std::endl;
    }
}




*/