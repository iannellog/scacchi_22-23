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

            first_col= self.posizione[1]
            last_col = destinazione[1]
            last_row = ord(destinazione[0])
            first_row = ord(self.posizione[0])
            if first_row > last_row:
                first_row = last_row
                last_row = ord(self.posizione[0])
            rows_distance = abs(last_row - first_row)
            if first_col > last_col:
                first_col = last_col
                last_col = self.posizione[1]
            columns_distance = abs(last_col - first_col)
            #Verifico se i movimenti sono quelli consentiti (movimenti di torre e alfiere)
            if columns_distance == rows_distance:
                for i in range(1,columns_distance):
                        if not self.scacchiera.get_pezzo([chr(first_row+i), first_col+i]) == None:  # la casella è occupata
                            print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(first_row+i), first_col+i]).nome}) nella casella {chr(first_row+i)}{first_col+i}")
                            return False
                if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None:
                    print(f"La Regina ha mangiato il pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                    return True
                return True
            elif self.posizione[0]==destinazione[0]:
                first = self.posizione[1]+1 if self.posizione[1]+1 < destinazione[1] else destinazione[1]+1  # prima riga da esaminare
                last = destinazione[1] if self.posizione[1]+1 < destinazione[1] else self.posizione[1]  # ultma riga da esaminare
                for riga in range(first, last):
                    if not self.scacchiera.get_pezzo([destinazione[0], riga]) == None:  # la casella è occupata
                        print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([destinazione[0], riga]).nome}) nella casella {destinazione[0]}{riga}")
                        return False
                if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None:
                    print(f"La Regina ha mangiato il pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                    return True
                return True
            elif self.posizione[1]==destinazione[1]:
                first = ord(self.posizione[0])+1 if ord(self.posizione[0])+1 < ord(destinazione[0]) else ord(destinazione[0])+1  # prima colonna da esaminare
                last = ord(destinazione[0]) if ord(self.posizione[0])+1 < ord(destinazione[0]) else ord(self.posizione[0])  # ultma colonna da esaminare
                for col in range(first, last):
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