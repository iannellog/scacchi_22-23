from Pezzo import Pezzo
import string


class Alfiere(Pezzo):
    """
    implementa l'Alfiere
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
        if super().verifica_mossa(destinazione):
            if self.posizione[0] == destinazione[0] or self.posizione[1] == destinazione[1]:
                #la mossa è lungo la stessa riga o colonna , la partenza coincide con la destinazione
                print("La mossa non è legale,l'alfiere si muovere solo in diagonale ")
                return False
            elif not abs((string.ascii_uppercase.index(self.posizione[0]) - string.ascii_uppercase.index(destinazione[0]))) == abs(self.posizione[1] - destinazione[1]):
                #il modulo della differenza tra il numero righe e colonne deve essere uguale
                print("La mossa non è legale")
                return False
            else:

                return True