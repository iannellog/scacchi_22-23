#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:10:02 2022

@author: iannello
"""

class Pezzo:
    """
    modella il generico pezzo del gioco
    """
    def __init__(self, colore, posizione=None, nome=None):
        """
        costruttore

        Parameters
        ----------
        colore : string
            indica il colore: bianco ('W') o nero ('B')
        posizione : coppia di coordinate (list)
            Posizione del pezzo sulla scacchiera. 
            Il default è None.
        nome : string
            Nome del pezzo. 
            Il default è None.

        Returns
        -------
        None.

        """
        self.colore = colore
        self.posizione = posizione
        self.nome = nome
        self.graphic_rep = '\u29bf' if self.colore == 'W' else '\u29be'

    def get_graphic_rep(self):
        """
        ritorna il simbolo grafico da usare per rappresentare
        il pezzo sulla scacchiera in forma visuale
        Returns
        -------
        string: il simbolo grafico consiste in una stringa che può
        contenere i carateri UNICODE e/o caratteri di controllo per
        il terminale
        """
        return self.graphic_rep

    def muovi(self, destinazione):
        """
        muove il pezzo

        Parameters
        ----------
        destinazione : coppia di coordinate (list)
            posizione di destinazione della mossa

        Returns
        -------
        bool
        indica se la mossa è legale o no

        """
        self.posizione = destinazione
        return True  # per ora la mossa è sempre legale
    
    def metti(self, posizione):
        """
        mette il pezzo sulla scacchiera nella posizione indicata

        Parameters
        ----------
        destinazione : coppia di coordinate (list)
            posizione in cui mettere il pezzo

        Returns
        -------
        None.

        """
        self.posizione = posizione
    
    def togli(self):
        """
        toglie il pezzo dalla scacchiera

        Returns
        -------
        None.

        """
        self.posizione = None