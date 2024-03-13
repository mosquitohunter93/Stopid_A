import pygame

###
#
# Class: Cell
#
# Jede zelle kann den Zustand 1 (Lebendig) oder 0 (Tot haben). Selbst verwaltet,
# kann sich auf Befehl des übergeordneten Automaten zeichnen und updaten.
#
###
class Cell():
    def __init__(self, screen, rect, cellState):
        self.screen = screen
        self.state = cellState
        self.oldState = cellState
        self.rect = rect
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    def draw(self):
        if self.state == 1:
            pygame.draw.rect(self.screen, "black", self.rect)
        else:
            pygame.draw.rect(self.screen, "white", self.rect)
        
    def getOldState(self):
        return self.oldState

    ###
    # Setzt die klassischen Regeln nach Conway um.
    ###
    def update(self):
        livingNeighbors = 0
        for c in self.neighbors:
            if c.getOldState() == 1:
                livingNeighbors += 1
        
        if self.oldState == 0 and livingNeighbors == 3:
            self.state = 1
        elif self.oldState == 1 and livingNeighbors < 2:
            self.state = 0
        elif self.oldState == 1 and livingNeighbors > 3:
            self.state = 0
        else:
            self.state = self.oldState

    def postUpdate(self):
        self.oldState = self.state;