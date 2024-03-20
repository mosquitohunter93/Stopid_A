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
class Automaton:
    def __init__(self, screen):
        self.cells = {}
        self.create_grid(screen)

    def create_grid(self, screen):
        cell_size = 500 / 10
        for y in range(10):
            for x in range(10):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                self.cells[(x, y)] = Cell(screen, rect, self.generateRandomCell())
        print(self.cells)
        
        # Nachdem alle Zellen erzeugt wurden, können Referenzen zu den Nachbarn hergestellt werden
        # Jede Zelle bekommt eine Liste mit Referenzen zu ihren 8 Nachbarn überreicht, die sie speichert
        for check_cell in self.cells:
            x, y = check_cell
            neighbors = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    coordinates = ((x + dx) % 10, (y + dy) % 10)
                    neighbors.append(self.cells.get(coordinates))
            self.cells[check_cell].setNeighbors(neighbors)
        
        self.lastUpdate = 0
        
    def generateRandomCell(self):
        return randint(0,1)
    
    def getValidCell(self, x, y):
        x = x % 10
        y = y % 10
        return self.cells.get((x, y))
    
    # Jede Zelle zeichnet sich selbst, danach werden alle Zellen ihren aktuellen Stand
    # in den oldState übertragen. So wird eine weitere Schleife durch alle Zellen einge-
    # spart.
    def draw(self):
        for coordinates in self.cells:
            self.cells[coordinates].draw()
            self.cells[coordinates].postUpdate()
    
    # Zählt die Zeit seit dem letzten Update des Automaten. Sind mehr als
    # 1000ms vergangen, so werden alle Zellen geupdatet.
    def update(self, deltaT):
        self.lastUpdate += deltaT
        if (self.lastUpdate > 1000):
            self.lastUpdate = 0

            for coordinates in self.cells:
                self.cells[coordinates].update()

