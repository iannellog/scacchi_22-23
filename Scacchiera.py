#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:19:01 2022

@author: iannello
"""

class Scacchiera:
    """
    """
    def __init__(self):
        """
        la scacchiera è rappresentata da due dizionari di liste
        che rappresentano le 64 posizioni attraverso coordinate
        formate da una lettera in ['A', 'H'] e da un numero in [1, 8]
        il primo dizionario memorizza se una casella è non occupata 
        (None) o è occupata (riferimento al pezzo che la occupa)
        il secondo dizionario serve per una facile visualizzazione 
        dello stato della scacchiera
        
        Nell'accesso alle liste che rappresentano le colonne
        della scacchiera bisogna sottrarre 1 perchè gli indici
        delle liste partono da 0
        
        INV: i due dizionari devono essere mantenuti coerenti

        Returns
        -------
        None.

        """
        self.pezzi = {'A': [None]*8,  # memorizza gli oggetti 
                      'B': [None]*8,  # posizionati sulla scacchiera
                      'C': [None]*8,
                      'D': [None]*8,
                      'E': [None]*8,
                      'F': [None]*8,
                      'G': [None]*8,
                      'H': [None]*8}
        self.piano = {'A': [' ']*8,   # meorizza una rappresentazione
                      'B': [' ']*8,   # visualizzabile della scacchiera
                      'C': [' ']*8,
                      'D': [' ']*8,
                      'E': [' ']*8,
                      'F': [' ']*8,
                      'G': [' ']*8,
                      'H': [' ']*8}
         
        
    def togli(self, posizione):
        """
        toglie un pezzo dalla scacchiera e lo sostituisce con None

        Parameters
        ----------
        posizione : coppia di coordinate (list)
            posizione da liberare.

        Returns
        -------
        None.

        """
        self.pezzi[posizione[0]][posizione[1]-1] = None
        self.piano[posizione[0]][posizione[1]-1] = ' '
    
    def metti(self, pezzo, posizione):
        """
        posiziona un pezzo sulla scacchiera

        Parameters
        ----------
        pezzo : Pezzo
            pezzo da posizionare
        posizione : coppia di coordinate
            posizione in cui posizionare il pezzo

        Returns
        -------
        None.

        """
        self.pezzi[posizione[0]][posizione[1]-1] = pezzo
        self.piano[posizione[0]][posizione[1]-1] = 'x'
    
    def get_pezzo(self, posizione):
        """
        retituisce un riferimento al pezzo che si trova 
        nella posizione indicata

        Parameters
        ----------
        posizione : coppia di coordinate
            posizione del pezzo

        Returns
        -------
        TYPE Pezzo
            pezzo posizionato nella posizione indicata

        """
        return self.pezzi[posizione[0]][posizione[1]-1]
    
    def visualizza(self):
        """
        visualizza sullo standard output lo stato della scacchiera

        Returns
        -------
        None.

        """
        for col in self.piano.keys():
            print(f'{col} | {self.piano[col]}')
        