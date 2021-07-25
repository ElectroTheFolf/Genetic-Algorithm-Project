# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 15:04:21 2021

@author: Brack
"""

class Place:
    #food (0-50) builds strength for monsters
    food = 0
    
    #danger level (0 - 100) determines how much heath depletes the monsters
    danger = 0
    
    #has trap instantly kills a monster
    hasTrap = False
    
    def __init__(self, food, danger, hasTrap):
        self._food = food
        self._danger = danger
        self._hasTrap = hasTrap
        
    def food(self):
        return self._food
    
    def set_food(self,food):
        self._food = food
    
    def danger(self):
        return self._danger
    
    def set_danger(self,danger):
        self._danger = danger
    
    def hasTrap(self):
        return self._hasTrap
    
    def set_trap(self,hasTrap):
        self._hasTrap = hasTrap
    
    
    
    def __str__(self):
        return f"Place Stats: \nFood amount(0-50): {self._food} \ndanger level(0-100): {self._danger} \nHas a Trap: {self._hasTrap}\n"