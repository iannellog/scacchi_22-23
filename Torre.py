#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:10:02 2022

@author: iannello
"""

from Pezzo import Pezzo


class Torre(Pezzo):
    """
    implementa la Torre
    """

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Torre')
        self.graphic_rep = '\u2656' if self.colore == 'W' else '\u265c'

    def verifica_mossa(self, destinazione):
        """
        verifica se la Torre può essere mosso alla destinazione

        Parameters
        ----------
        destinazione : coppia di coordinate (list)
            posizione di destinazione della mossa

        Returns
        -------
        bool
        indica se la mossa è legale o no

        """
        if super().verifica_mossa(destinazione):  # le condizioni generiche sono verificate
            if self.posizione[0] == destinazione[0]:  # la mossa è lungo la stessa colonna
                for riga in range(self.posizione[1]+1, destinazione[1]):
                    if not self.scacchiera.get_pezzo([destinazione[0], riga]) == None:
                        print(f"\u00c8 presente un pezzo ({self.scacchiera.get_pezzo([destinazione[0], riga]).nome}) nella casella {[destinazione[0], riga]}")
                        return False
                return True
            elif self.posizione[1] == destinazione[1]:  # la mossa è lungo la stessa riga
                return True
            else:
                return False
        else:
            return False
