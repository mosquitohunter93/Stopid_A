from UIManager import UIManager
from Automaton import Automaton

running = True
ui = UIManager()

automaton = Automaton(ui.getScreen())

while running:
    running = ui.update()
    automaton.update(ui.getDeltaT())
    automaton.draw()
    

ui.quit()