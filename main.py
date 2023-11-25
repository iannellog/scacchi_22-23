#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:42:39 2022

@author: iannello

"""

from Scacchiera import Scacchiera
from Pezzo import Pezzo
from Torre import Torre
from Cavallo import Cavallo


def in_board(posizione):
    """
    verifica che la posizione sia all'intgerno della scacchiera
    Parameters
    ----------
    posizione: coppia di coordinate

    Returns
    -------
    bool
        True se le coordinate corrispondono a una casella della
        scacchiera, False altrimenti
    """
    return posizione[0] in {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'} and \
           posizione[1] in range(1, 9)


def get_mossa():
    """
    acquisisce una mossa dallo standard input o termina il programma
    La mossa deve essere fornita nel formato:
        
        posizione_di_partenza posizione_di_destinazione
        
    dove una posizione è una coppia formata da una lettera
    in ['A', 'H'] e da una cifra in [1, 8]
    le due posizioni devono essere separate da un solo spazio

    se la lunghezza della stringa fornita in input è diversa
    da 5 il programma viene terminato

    Returns
    -------
    list
        posizione di partenza
    list
        posizione di destinazione

    """
    while True:
        mossa = input("Dammi la mossa: ")
        if not len(mossa) == 5:  # l'input non è una mossa
            exit(0)              # termina il programma
        partenza = [mossa[0].upper(), int(mossa[1])]
        destinazione = [mossa[3].upper(), int(mossa[4])]
        if in_board(partenza) and in_board(destinazione):
            return partenza, destinazione
        else:
            print(f'La partenza e/o la destinazione della mossa {mossa} non corrispondono a caselle della scacchiera')

def posizionaPezzi():
    #vengono posizionate prima le pedine bianche
    scacchiera.metti(Torre('W'), ['A',1])
    scacchiera.metti(Torre('W'), ['H', 1])
    scacchiera.metti(Cavallo('W'),['B',1])
    scacchiera.metti(Cavallo('W'),['G',1])

    #vengono posizionate le pedine nere
    scacchiera.metti(Torre('B'), ['A',8])
    scacchiera.metti(Torre('B'), ['H', 8])
    scacchiera.metti(Cavallo('B'),['B',8])
    scacchiera.metti(Cavallo('B'),['G',8])



if __name__ == "__main__":
    # setup del gioco
    scacchiera = Scacchiera()
    # posizione 4 pezzi bianchi nelle prime 4 righe della colonna A
    posizionaPezzi()

    scacchiera.visualizza()
    print()

    # inizia il gioco
    while True:
        while True:
            # acquisisce mossa da fare
            (partenza, destinazione) = get_mossa()
            # recupera il pezzo da muovere
            pezzo = scacchiera.get_pezzo(partenza)
            if pezzo is None:  # la mossa parte da una casella vuota
                print(f'La mossa non è valida: la casella di partenza è vuota')
            elif pezzo.verifica_mossa(destinazione):  # la mossa è legale
                break
        # esegui mossa sulla scacchiera
        if not scacchiera.get_pezzo(destinazione) is None:  # la casella è occupata
            scacchiera.togli(destinazione)  # "mangia" il pezzo che occupa la casella
        scacchiera.togli(partenza)
        scacchiera.metti(pezzo, destinazione)

        scacchiera.visualizza()
        print()
