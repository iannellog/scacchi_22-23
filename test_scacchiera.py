import unittest
from Scacchiera import Scacchiera
from Pezzo import Pezzo


class MyTestCase(unittest.TestCase):
    def test_coherence_board(self):
        """
        test che i pezzi sono collocati in modo coerente sulla
        scacchiera
        """
        scacchiera = Scacchiera()
        # posizione 4 pezzi bianchi nelle prime 4 righe della colonna A
        for i in range(1, 5):
            scacchiera.metti(Pezzo('W', nome='Pezzo'), ['A', i])
        # verifica coerenza dei dati dopo il posizionamento
        for col in scacchiera.pezzi:
            for pezzo, row in zip(scacchiera.pezzi[col], range(1, 9)):
                if not pezzo == None:
                    self.assertEqual(pezzo.posizione, [col, row])

    def test_coherence_move(self):
        scacchiera = Scacchiera()
        # posiziona il pezzo sulla scacchiera
        scacchiera.metti(Pezzo('W', nome='Pezzo'), ['A', 1])
        # muove il pezzo
        pezzo = scacchiera.get_pezzo(['A', 1])
        scacchiera.togli(['A', 1])
        scacchiera.metti(pezzo, ['H', 8])
        # verifica coerenza dei dati dopo la mossa
        self.assertEqual(scacchiera.get_pezzo(['H', 8]).posizione, ['H', 8])

    def test_capture(self):
        scacchiera = Scacchiera()
        # posiziona due pezzi sulla scacchiera
        scacchiera.metti(Pezzo('W', nome='Pezzo'), ['A', 1])
        scacchiera.metti(Pezzo('B', nome='Pezzo'), ['H', 8])
        pezzo = scacchiera.get_pezzo(['H', 8])
        # verifica se la casella di destinazione è occupata
        if not pezzo == None:
            scacchiera.togli(['H', 8])
        # muove il pezzo
        scacchiera.togli(['A', 1])
        scacchiera.metti(Pezzo('B', nome='Pezzo'), ['H', 8])
        # verifica coerenza dei dati dopo la mossa
        self.assertEqual(pezzo.posizione, None)
        self.assertEqual(pezzo.scacchiera, None)


if __name__ == '__main__':
    unittest.main()
