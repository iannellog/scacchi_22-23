from Pezzo import Pezzo


class alfiere(Pezzo):
    """
    implementa l'alfiere
    """

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'alfiere')
        #
        self.graphic_rep = '\u2657' if self.colore == 'W' else '\u265d'

    def verifica_mossa(self, destinazione):
        """
                verifica se l'alfiere può essere mosso alla destinazione

                Parameters
                ----------
                destinazione : coppia di coordinate (list)
                    posizione di destinazione della mossa

                Returns
                -------
                bool
                indica se la mossa è legale o no

             """
        # se tutte le condizioni precedenti sono verificati allora entra e verifia anche queste n
        y = ord(self.posizione[0])
        y1 = ord(destinazione[0])
        x = self.posizione[1]
        x1 = destinazione[1]

        if super().verifica_mossa(destinazione):  # le condizioni generiche sono verificate

            if (self.posizione[0] == destinazione[0] or self.posizione[1] == destinazione[1]):
                print("Mossa non valida, l'alfiere si può muovere solo lungo la diagonale #1")
                return False

            elif not (abs(y - y1)) == (abs(x - x1)):
                print(y, y1, x, x1)

                print("Mossa non valida, l'alfiere si può muovere solo lungo la diagonale #2")
                return False
            # per poterti muovere , la differenaza in modulo tra il numero di righe e colonne deve essere uguale
            # --> cosi mi muovo sulla diagonale

            # verifichare che durante il movimento l'alfiere non incotra pedine durante il percorso,
            # la verifica sulla casella destinazione è già presente in verifica mossa su pezzo

            for i in range(abs(self.posizione[1] - destinazione[1]) - 1):
                if (destinazione[1] < self.posizione[1]) and (ord(destinazione[0]) < ord(self.posizione[0])):
                    pezzo = [chr(ord(self.posizione[0]) - i - 1), self.posizione[1] - i - 1]
                elif (destinazione[1] > self.posizione[1]) and (ord(destinazione[0]) < ord(self.posizione[0])):
                    pezzo = [chr(ord(self.posizione[0]) - i - 1), self.posizione[1] + i + 1]
                elif (destinazione[1] > self.posizione[1]) and (ord(destinazione[0]) > ord(self.posizione[0])):
                    pezzo = [chr(ord(self.posizione[0]) + i + 1), self.posizione[1] + i + 1]
                elif (destinazione[1] < self.posizione[1]) and (ord(destinazione[0]) > ord(self.posizione[0])):
                    pezzo = [chr(ord(self.posizione[0]) + i + 1), self.posizione[1] - i - 1]

                if not (self.scacchiera.get_pezzo(pezzo) == None):  # la destinazione è occupata

                    print('La casella è occupata da un pezzo')
                    return False

            print('La mossa è valida')
            return True

        return False
