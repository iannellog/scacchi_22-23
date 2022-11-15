import unittest
from Scacchiera import Scacchiera
from Pezzo import Pezzo
from Torre import Torre


class MyTestCase(unittest.TestCase):
    def test_mossa_semplice(self):
        scacchiera = Scacchiera()
        t = Torre('W')
        scacchiera.metti(t, ['D', 4])
        self.assertEqual(True, t.verifica_mossa(['D', 7]))  # prova mossa lungo righe crescenti
        self.assertEqual(True, t.verifica_mossa(['G', 4]))  # prova mossa lungo colonne crescenti
        self.assertEqual(True, t.verifica_mossa(['D', 1]))  # prova mossa lungo righe decrescenti
        self.assertEqual(True, t.verifica_mossa(['A', 4]))  # prova mossa lungo colonne decrescenti
        self.assertEqual(False, t.verifica_mossa(['A', 6]))  # prova mossa in direzione errata

    def test_mossa_con_altri_pezzi(self):
        scacchiera = Scacchiera()
        t = Torre('W')
        scacchiera.metti(t, ['D', 4])
        scacchiera.metti(Pezzo('W', nome='pezzo generico'), ['D', 6])
        scacchiera.metti(Pezzo('B', nome='pezzo generico'), ['D', 1])
        self.assertEqual(False, t.verifica_mossa(['D', 8]))  # prova mossa su casella occupata da un altro pezzo
        self.assertEqual(False, t.verifica_mossa(['D', 6]))  # prova mossa su casella occupata da un  pezzo dello stesso colore
        self.assertEqual(True, t.verifica_mossa(['D', 1]))  # prova mossa su casella occupata da un  pezzo di altro colore

if __name__ == '__main__':
    unittest.main()
