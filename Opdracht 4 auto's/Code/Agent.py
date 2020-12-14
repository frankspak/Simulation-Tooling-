from mesa import Agent
import random

class CarAgent(Agent):

    max_snelheid = 5

    # Elke auto begint met een random snelheid, van 0 T/M 5.
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.snelheid = random.randint(0, 5)


    def optrekken(self):
        if self.snelheid < CarAgent.max_snelheid:
            self.snelheid += 1

        return self.snelheid

    def remmen(self):
        self.snelheid -= 1

        return self.snelheid

    def move(self):
        pass

    def role_of_randomization(self):
        if self.snelheid > 1:
            if random.randint(0,1) == 1:
                self.snelheid -= 1
            else:
                self.snelheid = self.snelheid

        return self.snelheid