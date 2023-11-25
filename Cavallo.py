from Pezzo import Pezzo

class Cavallo(Pezzo):
    #implementazione del cavallo

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Cavallo')
        self.graphic_rep = '\u2658' if self.colore == 'W' else '\u265E'

    def verifica_mossa(self, destinazione):
        """ la sintassi è la stessa usata nella funzione verifica_mossa della classe Torre"""

        if super().verifica_mossa(destinazione):  # le condizioni generiche sono verificate
            #nota la destinazione, calcolo dove il cavallo puo' andare
            possible_position=self.possibiliPosizioni()
            if destinazione in possible_position:
                if not self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]) == None:  # la casella è occupata
                    print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([destinazione[0], destinazione[1]]).nome}) nella casella {destinazione[0]}{destinazione[1]}")
                    return False
                return True
            else:
                print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
                return False
        else:
            print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Cavallo')
            return False


    def possibiliPosizioni(self):
        """
        ogni cavallo si puo spostare
            -o DUE righe in su o giu e UNA colonna a destra o sinistra
            -o UNA riga su o giu e DUE colonne a destra o sinistra
        per un totale di 8 possibili posizioni
        nota la posizione iniziale popoliamo la lista delle possibili posizioni facendo attenzione a non aggiungere
        posizioni fuori dalla scacchiera
        :return:
        lista delle possibili posizioni che il cavallo puo occupare
        """
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        cols = [1, 2, 3, 4, 5, 6, 7, 8]
        lista_possibili_posizioni = [];
        indice_riga = rows.index(self.posizione[0])
        indice_col = cols.index(self.posizione[1])

        indice_riga_succ = indice_riga + 1
        indice_riga_prec = indice_riga - 1
        indice_col_succ = indice_col + 1
        indice_col_prec = indice_col - 1

        indice_riga_2succ = indice_riga + 2
        indice_riga_2prec = indice_riga - 2
        indice_col_2succ = indice_col + 2
        indice_col_2prec = indice_col - 2
        r = range(0, 8)
        if indice_riga_2succ in r:
            if indice_col_prec in r:
                lista_possibili_posizioni.append([rows[indice_riga_2succ], cols[indice_col_prec]])
            if indice_col_succ in r:
                lista_possibili_posizioni.append([rows[indice_riga_2succ], cols[indice_col_succ]])
        if indice_riga_succ in r:
            if indice_col_2prec in r:
                lista_possibili_posizioni.append([rows[indice_riga_succ], cols[indice_col_2prec]])
            if indice_col_2succ in r:
                lista_possibili_posizioni.append([rows[indice_riga_succ], cols[indice_col_2succ]])
        if indice_riga_prec in r:
            if indice_col_2prec in r:
                lista_possibili_posizioni.append([rows[indice_riga_prec], cols[indice_col_2prec]])
            if indice_col_2succ in r:
                lista_possibili_posizioni.append([rows[indice_riga_prec], cols[indice_col_2succ]])
        if indice_riga_2prec in r:
            if indice_col_prec in r:
                lista_possibili_posizioni.append([rows[indice_riga_2prec], cols[indice_col_prec]])
            if indice_col_succ in r:
                lista_possibili_posizioni.append([rows[indice_riga_2prec], cols[indice_col_succ]])

        return lista_possibili_posizioni
