#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:10:02 2022

@author: stefanoperone01
"""

from Pezzo import Pezzo


class Cavallo(Pezzo):
    """
    implementa il Cavallo
    """

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Cavallo')
        self.graphic_rep = '\u2658' if self.colore == 'W' else '\u265e'

    def verifica_mossa(self, destinazione):
        """
        verifica se il Cavallo può essere mosso alla destinazione

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
        #Verifico che i movimenti siano quelli possibili per il Cavallo
            if ord(destinazione[0]) == ord(self.posizione[0])+2 or ord(destinazione[0]) == ord(self.posizione[0])-2:
                if destinazione[1] == self.posizione[1]+1 or destinazione[1] == self.posizione[1]-1:
                    if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None:
                        print(f"Il Cavallo ha mangiato il pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                        return True
                    return True
                print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
                return False
            elif destinazione[1] == self.posizione[1]+2 or destinazione[1] == self.posizione[1]-2:
                if ord(destinazione[0]) == ord(self.posizione[0])+1 or ord(destinazione[0]) == ord(self.posizione[0])-1:
                    if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None:
                        print(f"Il Cavallo ha mangiato il pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                        return True
                    return True
                print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
                return False
            else:
                print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
                return False
        else:
            print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
            return False