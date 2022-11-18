#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:21:30 2022

@author: stefanoperone01
"""

from Pezzo import Pezzo


class Re(Pezzo):
    """
    implementa il Re
    """

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Re')
        self.graphic_rep = '\u2654' if self.colore == 'W' else '\u265a'

    def verifica_mossa(self, destinazione):
        """
        verifica se il Re può essere mosso alla destinazione

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

            #if self.colore=='W':
            first_col = self.posizione[1]
            last_col = destinazione[1]
            last_row = ord(destinazione[0])
            first_row = ord(self.posizione[0])
            if first_col < last_col:
                 first_col = last_col
                 last_col = self.posizione[1]
            if first_row < last_row:
                 first_row = last_row
                 last_row = ord(self.posizione[0])
            if (first_col == last_col + 1 or first_col == last_col - 1 or first_col == last_col) and (first_row == last_row + 1 or first_row == last_row - 1 or first_row == last_row): 
                for row in range(first_row+1, last_row):
                    if not self.scacchiera.get_pezzo([chr(row), destinazione[1]]) == None:  # la casella è occupata
                        print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(row), destinazione[1]]).nome}) nella casella {chr(row)}{destinazione[1]}")
                        return False
                # for col in range(first_col+1, last_col+1):
                #     if not self.scacchiera.get_pezzo([destinazione[0],chr(col)]) == None:  # la casella è occupata
                #         print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([destinazione[0], chr(col)]).nome}) nella casella {destinazione[0]}{chr(col)}")
                #         return False
                if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None: #and self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).colore!=self.colore:
                    #self.posizione = destinazione
                    print(f"Il pedone ha mangiato il pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                    return True
                #elif self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).colore==self.colore:
                    #print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) dello stesso colore nella casella {destinazione[0]}{destinazione[1]}")
                    #return False
                return True
            else:
                print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Re")
                return False
        else:
            print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Re")
            return False