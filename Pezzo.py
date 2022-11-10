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
            indica il colore: bianco ('w') o nero ('b')
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