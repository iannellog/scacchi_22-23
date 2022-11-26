#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:55:48 2022

@author: stefanoperone01
"""

from Pezzo import Pezzo


class Alfiere(Pezzo):
    """
    implementa l'alfiere
    """

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Alfiere')
        self.graphic_rep = '\u2657' if self.colore == 'W' else '\u265d'

    def verifica_mossa(self, destinazione):
        """
        verifica se l'Alfiere può essere mosso alla destinazione

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
            #verifico che lo spostamento sia sulla diagonale
            if columns_distance == rows_distance and columns_distance>0:
                #verifico che le caselle in cui passare siano libere
                for i in range(1,columns_distance):
                    if not self.scacchiera.get_pezzo([chr(first_row+i), first_col+i]) == None:  # la casella è occupata
                        print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(first_row+i), first_col+i]).nome}) nella casella {chr(first_row+i)}{first_col+i}")
                        return False
                #se nella casella finale c'è un pezzo avversario, stampo che l'ho mangiato
                if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None:
                    print(f"L'Alfiere ha mangiato il pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                    return True
                return True
            else:
                print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per l'Alfiere")
                return False
        else:
            print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per l'Alfiere")
            return False