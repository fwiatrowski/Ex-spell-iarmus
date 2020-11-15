# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:31:39 2020

@author: Ian Cheung
"""
##Creating objects for the game

class Player(object): 
    def __init__(self, Team, Health, Stamina, Level, State, DamageCaused, Casted):
        self.Team = Team
        self.Health = Health
        self.Stamina = Stamina
        self.Level = Level
        self.State = State
        self.DamageCaused = DamageCaused 
        self.SpellQ = []
        
    def Cast(self, Spell): #method for the player to cast a spell, saves the spell object into Player.Casted
        if not self.SpellQ:
            if self.Level >= Spell.LevelUnlocked:
                if self.Stamina >= Spell.Stamina:
                    self.Casted = Spell
                    self.Stamina -= Spell.StaminaCost
                    self.DamageCaused += Spell.Damage
                elif self.Stamina < Spell.Stamina:
                    self.SpellQ.append(Spell)
            else print("you cannot cast this spell boy")

        if self.SpellQ:
            if self.Level >= Spell.LevelUnlocked:
                if self.Stamina >= self.SpellQ[0].Stamina:
                    self.Casted = self.SpellQ[0]
                    self.Stamina -=  self.SpellQ[0].StaminaCost
                    self.DamageCaused -= self.SpellQ[0].Damage
                    self.SpellQ.append(Spell)
                else:
                    self.SpellQ.append(Spell)
            else print("you cannot cast this spell you kid")
                
    def Hit(self, Spell): #method for taking damage
        self.Health -= Spell.Damage
        if self.Health <= 0: 
            self.Death()
            
    def Level(self): #Increases their level if the
        if  0<= self.DamageCaused <10:
            self.Level = 1
        if  11< self.DamageCaused <20:
            self.Level = 2
        if  21 < self.DamageCaused <30:
            self.Level = 3
        if  31<= self.DamageCaused <40:
            self.Level = 4
        if  self.DamageCaused > 41:
            self.Level = 5
            
    def StaminaUpdate(self): #Updates Stamina by 1 every time function is called
         self.Stamina +=1 #Scale this depending on how often the state is updated
            
    def Update(self): #Updates player state 
        self.Level()
        self.StaminaUpdate()
        
 
    
