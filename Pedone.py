#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:26:52 2022

@author: stefanoperone01
"""

from Pezzo import Pezzo

class Pedone(Pezzo):
    
    """
    implementa il Pedone
    """
    
    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Pedone')
        self.graphic_rep = '\u2659' if self.colore == 'W' else '\u265f'

    def verifica_mossa(self, destinazione):
        """
        verifica se il Pedone può essere mosso alla destinazione

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

            if self.colore=='W':
                if self.posizione[1] == destinazione[1]:  # la mossa è lungo la stessa colonna
                    partenza=ord(self.posizione[0])
                    arrivo=ord(destinazione[0])
                    #verifico se lo spostamento è di una sola unità (o di due nel caso di prima mossa)
                    if arrivo==partenza+1 or (arrivo==partenza+2 and partenza==ord('B')):
                        #in tal caso verifico che la cella (o le due celle in caso di prima mossa) non sia occupata
                        for col in range(partenza+1, arrivo+1):
                            if not self.scacchiera.get_pezzo([chr(col), destinazione[1]]) == None:  # la casella è occupata
                                print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(col), destinazione[1]]).nome}) nella casella {chr(col)}{destinazione[1]}")
                                return False
                            else:
                                return True
                    else:
                        print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Pedone')
                        return False
                elif self.posizione[1]==destinazione[1]+1 or self.posizione[1]==destinazione[1]-1:
                    partenza=ord(self.posizione[0])
                    arrivo=ord(destinazione[0])
                    if arrivo==partenza+1:
                        if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None:
                            print(f"Il pedone ha mangiato il pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                            return True
                    return False
                else:
                    print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Pedone')
                    return False
                
            if self.colore=='B':
                if self.posizione[1] == destinazione[1]:  # la mossa è lungo la stessa colonna
                    partenza=ord(self.posizione[0])
                    arrivo=ord(destinazione[0])
                    if arrivo==partenza-1 or (arrivo==partenza-2 and partenza==ord('G')):
                        for col in range(arrivo+1, partenza+1):
                            if not self.scacchiera.get_pezzo([chr(col), destinazione[1]]) == None:  # la casella è occupata
                                print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(col), destinazione[1]]).nome}) nella casella {chr(col)}{destinazione[1]}")
                                return False
                            else:
                                return True
                    else:
                        print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Pedone')
                        return False
                elif self.posizione[1]==destinazione[1]+1 or self.posizione[1]==destinazione[1]-1:
                    partenza=ord(self.posizione[0])
                    arrivo=ord(destinazione[0])
                    if arrivo==partenza-1:
                        if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None:
                            print(f"Il pedone ha mangiato il pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                            return True

                    return False
                else:
                    print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Pedone')
                              
        else:
            print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Pedone')
            return False
