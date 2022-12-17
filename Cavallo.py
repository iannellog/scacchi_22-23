# -*- coding: utf-8 -*-
"""
"""

from Pezzo import Pezzo

class Cavallo(Pezzo):
    
    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Cavallo')
        self.graphic_rep = '\u265e' if self.colore == 'B' else '\u2658'
    
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
    #non può rimanere lungo la sua stessa lettera: 
        #può andare o 1 o 2 lettere sia avanti che indietro
        righe_possibili={'A':['B','C'],'B':['A','C','D'],'C':['A','B','D','E'],'D':['B','C','E','F'],'E':['C','D','F','G'],'F':['D','E','G','H'],'G':['E','F','H'],'H':['G','H']}
        #verifico che nella casella di arrivo non c'è un mio pezzp
        
        if super().verifica_mossa(destinazione):
            #verifico che la mossa non stia sulla stessa riga e stessa colonna
            if self.posizione[0] != destinazione[0] and self.posizione[1] != destinazione[1]:
                for i in range(len(righe_possibili[self.posizione[0]])):
                    if destinazione[0]==righe_possibili[self.posizione[0]][i]:
                        if destinazione[1]==self.posizione[1]+1 or destinazione[1]==self.posizione[1]+2 or destinazione[1]==self.posizione[1]-1 or destinazione[1]==self.posizione[1]-2:
                            return True
                        else:
                            print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
                            return False
                    else:
                        print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
                        return False                            
            else:
                print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
                return False
            
            #verifico che la mossa sia compresa fra la riga/colonna dopo e quella dopo ancora         
            
        else:
            print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
            return False
        
        
            
        
        
        
        
    

