import pygame

###
#
# Class: UIManager
#
# Erzeugt mittels PyGame ein Fenster und verwaltet dieses. Steuert zudem UI-Events
# (wie Klicks, Fenster schließen, ...).
# Hier wird außerdem die GameTime gesteuert.
#
###
class UIManager():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((500, 500))
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        pygame.display.flip()
        self.clock.tick(10)
        return True
    
    def getScreen(self):
        return self.screen;

    def getDeltaT(self):
        return self.clock.get_time()
    
    def quit(self):
        pygame.quit()