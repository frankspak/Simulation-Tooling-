from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

def wegen():
    pass

def auto_visualisatie(Agent):
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}
    return portrayal

grid = CanvasGrid(auto_visualisatie, 100, 1, 500, 500) # 100x1 grid in 500x500 pixels

server = ModularServer(#model,
                       [grid],
                       "#naam",
                       {"N":100, "width":10, "height":10})
server.port = 8521 # The default
server.launch()