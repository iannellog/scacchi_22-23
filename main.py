#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:42:39 2022

@author: iannello

"""

from Scacchiera import Scacchiera
from Pezzo import Pezzo


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
    mossa = input("Dammi la mossa: ")
    if not len(mossa) == 5:
        exit(0)
    return [mossa[0].upper(), int(mossa[1])], [mossa[3].upper(), int(mossa[4])]
 

if __name__ == "__main__":
    # setup del gioco
    scacchiera = Scacchiera()
    # posizione 4 pezzi bianchi nelle prime 4 righe della colonna A
    for i in range(1, 5):
        p = Pezzo('W')
        p.metti(['A', i])
        scacchiera.metti(p, ['A', i])
    # posizione 4 pezzi neri nelle prime 4 righe della colonna H
    for i in range(1,5):
        p = Pezzo('B')
        p.metti(['H', i])
        scacchiera.metti(p, ['H', i])

    scacchiera.visualizza()
    print()

    # inizia il gioco
    while True:
        while True:
            # acquisisce mossa da fare
            (partenza, destinazione) = get_mossa()
            # recupera il pezzo da muovere
            pezzo = scacchiera.get_pezzo(partenza)
            # muovi il pezzo sulla scacchiera
            if pezzo.muovi(destinazione):  # la mossa è legale
                break
            else:
                print(f'La mossa {partenza[0]}{partenza[1]}, {destinazione[0]}{destinazione[1]} non è legale')
        # esegui mossa sulla scacchiera
        scacchiera.togli(partenza)
        scacchiera.metti(pezzo, destinazione)

        scacchiera.visualizza()
        print()

