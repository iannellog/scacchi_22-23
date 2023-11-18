# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:30:39 2023

@author: Mattia
"""

from Pezzo import Pezzo
class Regina(Pezzo):

            def __init__(self, colore, posizione=None):
                super().__init__(colore, posizione, 'Regina')
                self.graphic_rep = '\u265B' if self.colore == 'W' else '\u2655'

            def verifica_mossa(self, destinazione):
                # creo un dict colonne_num dove assoccio ad ogni lettera un valore numerico
                colonne_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
                colonne_lett = {1: 'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7: 'G', 8:'H' }

                
                if super().verifica_mossa(destinazione):
                    # Calcola la differenza tra le coordinate

                    #fa la differenza in valore assoluto tra i numeri corrispondenti alle lettere
                    diff_colonne = abs(colonne_num[self.posizione[0]] - colonne_num[destinazione[0]])
                    diff_righe = abs(self.posizione[1] - destinazione[1])

                    # Verifica se il movimento è lungo la stessa colonna o riga o diagonale
                    if diff_colonne == 0 or diff_righe == 0 or diff_colonne == diff_righe:
                        # Verifica che non ci siano pezzi lungo il percorso
                        #aggiunge 1 se ci spostiamo a dx o -1 se a sx
                        direzione_colonne = 1 if self.posizione[0] < destinazione[0] else -1
                        # aggiunge 1 se saliamo o -1 se scendiamo
                        direzione_righe = 1 if self.posizione[1] < destinazione[1] else -1



                        for i in range(1, max(diff_colonne, diff_righe)):
                            #quante colonne_num ci spostiamo
                            nuova_casella_col = colonne_num[self.posizione[0]] + i * direzione_colonne
                            #quante righe ci spostiamo
                            nuova_casella_rig = self.posizione[1] + i * direzione_righe


                            nuova_casella_col = colonne_lett[nuova_casella_col]

                            if not self.scacchiera.get_pezzo([nuova_casella_col, nuova_casella_rig]) is None:
                                print(
                                    f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([nuova_casella_col, nuova_casella_rig]).nome}) nella casella {nuova_casella_col}{nuova_casella_rig}")
                                return False

                        return True
                    else:
                        print(
                            f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per la Regina')
                        return False
                else:
                    print(
                        f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per la Regina')
                    return False
