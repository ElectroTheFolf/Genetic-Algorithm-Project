# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 15:01:11 2021

@author: Brack Harmon


"""

class Monster:
    #health points (0 - 100) if health is zero the monster is dead
    hp = 0
    
    #strength (0+) stronger monsters outcompete other monsters
    sx = 0
    
    #DNA determines which places the monster will go to
    dna = []
    
    #the unique number that is attached to the monster
    iden = 0
    
    def __init__(self,hp,sx,dna,iden): # __init__ is always used for a constructor
    
        self._hp = hp # the underscore prevents global usage of variable
        self._sx = sx
        self._dna = dna
        self._iden = iden
    
    def hp(self):
        return self._hp
    
    def set_hp(self,hp):
        self._hp = hp
    
    def sx(self):
        return self._sx
    
    def set_sx(self,sx):
        self._sx = sx
    
    def dna(self):
        return self._dna
    
    def set_dna(self,dna):
        self._dna = dna
    
    def iden(self):
        return self._iden
    
    def __str__(self):
        return f"Monster stats: \nHealth(0-100): {self._hp} \nStrength(0+): {self._sx} \nID: {self._iden}\n"
    
    
    
    