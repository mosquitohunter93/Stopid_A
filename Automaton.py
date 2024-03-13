from Cell import Cell
from random import randint
import pygame

###
#
# Class: Automaton
#
# Konstruktor erzeugt ein 10x10 Grid von Zellen (Cell) und gibt diesen zufällige Startwerte.
# Der Automaton kann den aktuellen Zustand des Automaten ausgeben (draw), indem er die Zellen 
# beauftragt sich selbst zu zeichnen.
# Der Automaton stößt die nächste Iteration der zellen an (Update). Dies geschieht automatisch 
# alle 1000ms.
# 
# Da Zellen (Cell) nur Zugriff auf ihre eigenen Daten haben, gibt der Automat
# einen Verweis auf die Nachbarschaft der Zelle nach der Konstruktion aller Zellen.
# Da diese sich nicht ändert, bleibt die Referenz über die Laufzeit statisch.
#
###
class Automaton():
    def __init__(self, screen):
        self.cells = []

        # Zellen wissen nicht wo sie im Grid sind, sie bekommen ein pygame
        # Rect übergeben, welches sie entsprechend einfärben. Das Rect-Objekt kennt
        # seine Position auf dem Screen.
        for y in range(10):
            row = []
            for x in range(10):
                cellSize = 500/10
                rect = pygame.Rect(x*cellSize,y*cellSize,cellSize, cellSize)

                row.append(Cell(screen, rect, self.generateRandomCell()))
            self.cells.append(row)

        # Nachdem alle Zellen erzeugt wurden, können Referenzen zu den Nachbarn hergestellt werden
        # Jede Zelle bekommt eine Liste mit Referenzen zu ihren 8 Nachbarn überreicht, die sie speichert
        for y in range(10):
            for x in range(10):
                cell = self.getValidCell(x,y)

                neighbors = []
                neighbors.append(self.getValidCell(x-1,y-1))
                neighbors.append(self.getValidCell(x-1,y))
                neighbors.append(self.getValidCell(x-1,y+1))
                neighbors.append(self.getValidCell(x,y-1))
                neighbors.append(self.getValidCell(x,y+1))
                neighbors.append(self.getValidCell(x+1,y-1))
                neighbors.append(self.getValidCell(x+1,y))
                neighbors.append(self.getValidCell(x+1,y+1))

                cell.setNeighbors(neighbors)
        
        self.lastUpdate = 0
        
    def generateRandomCell(self):
        return randint(0,1)
    
    def getValidCell(self, x, y):
        if (x < 0):
            x = 9
        if (x > 9):
            x = 0
        
        if (y < 0):
            y = 9
        if (y > 9):
            y = 0
        
        return self.cells[y][x]
    
    # Jede Zelle zeichnet sich selbst, danach werden alle Zellen ihren aktuellen Stand
    # in den oldState übertragen. So wird eine weitere Schleife durch alle Zellen einge-
    # spart.
    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()
                cell.postUpdate()
    
    # Zählt die Zeit seit dem letzten Update des Automaten. Sind mehr als
    # 1000ms vergangen, so werden alle Zellen geupdatet.
    def update(self, deltaT):
        self.lastUpdate += deltaT
        if (self.lastUpdate > 1000):
            self.lastUpdate = 0

            for row in self.cells:
                for cell in row:
                    cell.update()

