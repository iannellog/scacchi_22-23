#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:55:48 2022

@author: stefanoperone01
"""

from Pezzo import Pezzo


class Regina(Pezzo):
    """
    implementa la Regina
    """

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Regina')
        self.graphic_rep = '\u2655' if self.colore == 'W' else '\u265b'

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

            distanza_col = abs(destinazione[1]-self.posizione[1])
            last = ord(destinazione[0])
            first = ord(self.posizione[0])
            distanza_righe = abs(last-first)
            #Verifico se i movimenti sono quelli consentiti (movimenti di torre e alfiere)
            if distanza_col == distanza_righe or self.posizione[0]==destinazione[0] or self.posizione[1]==destinazione[1]:
                for col in range(first+1, last):
                    if not self.scacchiera.get_pezzo([chr(col), destinazione[1]]) == None:  # la casella è occupata
                        print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(col), destinazione[1]]).nome}) nella casella {chr(col)}{destinazione[1]}")
                        return False
                if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None:
                    print(f"La Regina ha mangiato il pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                    return True
                return True
            else:
                print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per la Regina")
                return False
        else:
            print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per la Regina")
            return False