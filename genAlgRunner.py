# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 15:08:51 2021

@author: Brack
"""

import random
from Monster import Monster
from Place import Place
import numpy as np
import matplotlib.pyplot as plt

places = []
population = []
currid = 1
dnaSize = 16
popSize = 10000
iterations = 10

avgStrengths = []
popSizes = []
popSizes.append(popSize)

#main method handles main project functions
def main():
    firstGen(popSize)
    genPlaces(dnaSize)
    
    for i in range(iterations):
        #print(f"\nGeneration: {i}\n\n")
        start()
        removeDeadMonsters()
        compete()
        genChildren()
    
    displayStrengthData()
    displayPopData()
    
    
'''
    populates the world for the first generation

    n = number of monsters to start with
'''
def firstGen(n):
    global currid
    for i in range(n):
        dna = genDNA(dnaSize)
        m = Monster(100,0,dna,currid)
        currid += 1
        population.append(m)

'''
    generates random DNA by filling an array with random binary digits

    n = number of digitds of DNA
'''
def genDNA(n):
    dna = []
    for i in range(n):
        if random.randint(0, 1) == 0:
            dna.append(0)
        else:
            dna.append(1)
    return dna
        
   
'''
    generates world with places
    
    n = number of places to generate
'''
def genPlaces(n):
    for i in range(n):
        food = random.randint(0, 50)
        danger = random.randint(0, 5)
        hasTrap = random.randint(0,9) == 0
        p = Place(food,danger,hasTrap)
        places.append(p)
    
    
# start the next generation by having each monster go throght the places
def start():
    popLen = len(population)
    for i in range(popLen):
        m = population[i]
        dna = m.dna()
        for j in range(len(dna)):
            bit = dna[j]
            place = places[j]
            if bit == 1:
                #add strength
                m.set_sx(m.sx() + place.food())
                #reduce health
                m.set_hp(m.hp() - place.danger())
                
                if m.hp() < 0 or place.hasTrap():
                    m.set_hp(0)
                
            
#removes dead monsters from population
def removeDeadMonsters():
    i = 0
    while i < len(population):
        m = population[i]
        if m.hp() == 0:
            population.pop(i)
            i -= 1
        i += 1
        

'''
    runs a competition and returns the strongest monster
    

'''
def compete():
    i = 0
    
    if len(population) % 2 != 0:
        i = 1
    
    while i < len(population):
        m1 = population[i]
        m2 = population[i+1]
        if(m1.sx() > m2.sx()):
            population.pop(i+1)
        else:
            population.pop(i)
        i+=1
    popSizes.append(len(population))
    avgStrength()
'''

creates a new generation of children based on the parent's DNA

mutations can also happen if the threshold is reached

'''
def genChildren():
    global currid
    global population
    children = []
    i = 0
    if len(population) % 2 != 0:
        i = 1
    
    while i < len(population):
        m1 = population[i]
        m2 = population[i+1] 
        dna1 = []
        dna2 = []
        for j in range(dnaSize):
            if j < dnaSize/2:
                dna1.append(m1.dna()[j])
                dna2.append(m2.dna()[j])
            else:
                dna1.append(m2.dna()[j])
                dna2.append(m1.dna()[j])
        children.append(Monster(100,0,dna1,currid))
        currid += 1
        children.append(Monster(100,0,dna2,currid))
        currid += 1
        i += 2
    population = children
        
def avgStrength():
    sum = 0
    for i in range(len(population)):
        sum += population[i].sx()
    avgStrengths.append(sum/len(population))

   
#use the matplotlab package to display data on how the monsters survive the world
def displayStrengthData():
    x = np.arange(1,len(avgStrengths)+1)
    y = np.array(avgStrengths)
    plt.style.use('classic')
    plt.title("Population Strenghth over Time")
    plt.plot(x,y, color='red', marker = 'h')
    plt.xlabel("Generation")
    plt.ylabel("Average Strength of population")
    
    for x,y in zip(x,y):

        label = "{:.2f}".format(y)

        plt.annotate(label, # this is the text
                     (x,y), # these are the coordinates to position the label
                     textcoords="offset points", # how to position the text
                     xytext=(0,-10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    
    plt.show()

def displayPopData():
    x = np.arange(0,len(popSizes))
    y = np.array(popSizes)
    
    plt.style.use('classic')
    plt.title("Population Size over Time")
    plt.plot(x,y, color='blue', marker = 'h')
    plt.xlabel("Generation")
    plt.ylabel("Number of Monsters")
    
    for x,y in zip(x,y):

        label = "{:.2f}".format(y)

        plt.annotate(label, # this is the text
                     (x,y), # these are the coordinates to position the label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    
    plt.show()

#prints out every Monsterr
def printPop():
    for i in range(len(population)):
        print(population[i])
        
#prints out every Place
def printPlaces():
    for i in range(len(places)):
        print(places[i])
        
   
#run main method
if __name__ == '__main__': main()
    

