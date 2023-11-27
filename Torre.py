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
                # verifica che non ci siano pezzi tra la casella di partenza e quella di arrivo
                # per gestire corretamente il ciclo deve distinguere il caso di mossa per righe crescenti o decrescenti
                first = self.posizione[1]+1 if self.posizione[1]+1 < destinazione[1] else destinazione[1]+1  # prima riga da esaminare
                #posizione' incrementato di 1, se questo valore è minore  del primo carattere
                # di 'destinazione'; altrimenti, sarà il primo carattere di 'destinazione' ad incrementare di 1.
                last = destinazione[1] if self.posizione[1]+1 < destinazione[1] else self.posizione[1]  # ultma riga da esaminare
                for riga in range(first, last):
                    if not self.scacchiera.get_pezzo([destinazione[0], riga]) == None:  # la casella è occupata
                        print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([destinazione[0], riga]).nome}) nella casella {destinazione[0]}{riga}")
                        return False
                return True
            elif self.posizione[1] == destinazione[1]:  # la mossa è lungo la stessa riga
                # verifica che non ci siano pezzi tra la casella di partenza e quella di arrivo
                # per gestire corretamente il ciclo deve distinguere il caso di mossa per colonne crescenti o decrescenti
                first = ord(self.posizione[0])+1 if ord(self.posizione[0])+1 < ord(destinazione[0]) else ord(destinazione[0])+1  # prima colonna da esaminare
                last = ord(destinazione[0]) if ord(self.posizione[0])+1 < ord(destinazione[0]) else ord(self.posizione[0])  # ultma colonna da esaminare

                for col in range(first, last):
                    if not self.scacchiera.get_pezzo([chr(col), destinazione[1]]) == None:  # la casella è occupata
                        print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(col), destinazione[1]]).nome}) nella casella {chr(col)}{destinazione[1]}")
                        return False
                return True
            else:
                print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per la Torre')
                return False
        else:
            print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per la Torre')
            return False
