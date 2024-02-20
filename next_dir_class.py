#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
"""
nextDirClass - Fev/2024

Author: Ricardo Abuchaim - Contact: ricardoabuchaim@gmail.com
License: MIT

en:
Imagining a directory structure based on /X/Y/W/Z, where files are written to these directories.
The class below allows files to be balanced as evenly as possible. With this class it is also possible to generate 
the text used to create this directory tree at N levels, with characters from 0..9-A-F

pt-BR:
Imaginando uma estrutura de diretórios baseada em /X/Y/W/Z, onde os arquivos são gravados nesses diretórios. 
A classe abaixo, permite que os arquivos sejam balanceados da forma mais uniforme possível. Com essa classe também 
é possivel gerar o texto usado para a criação dessa arvore de diretórios em N niveis, com caracteres de 0..9-A-F

Usage example:

    nextDir = nextDirClass(dir_levels=4,random_start=True)
    while True:
        print(nextDir.get_next())


"""
import os, sys, time

import itertools, random
class nextDirClass():
    """Usage example:

        nextDir = nextDirClass(dir_levels=4,random_start=True)

        while True:

            print(nextDir.get_next())
    
    """
    def __init__(self,dir_levels:int=3,random_start=False):
        self.sequence = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F']
        self.level = [itertools.cycle(self.sequence) for _ in range(dir_levels)]
        if random_start:
            self.next = [next(itertools.islice(self.level[_],random.randint(0,dir_levels),None)) for _ in range(dir_levels)]
        else:
            self.next = ['1' for _ in range(dir_levels)]
    def get_next(self):
        """ Returns the text for the next directory 
        """
        for indexUp, (_,_) in enumerate(zip(self.next, reversed(self.next))):
            indexDown = len(self.next) - indexUp - 1
            if indexUp < len(self.next)-1:
                self.next[indexUp] = next(self.level[indexUp]) if (len([item for item in self.next[-indexDown:] if item == "F"]) == indexDown) else self.next[indexUp]
            else:
                self.next[indexUp] = next(self.level[indexUp])
        return f"/{'/'.join(map(str,self.next))}/"

nextDir = nextDirClass(dir_levels=4,random_start=True)
while True:
    print(nextDir.get_next())

