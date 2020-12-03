import mesa

class CarAgent(Agent):

    snelheid = 100
    max_snelheid = 100

    def auto(self):
        self.snelheid = CarAgent.snelheid

    def optrekken(self):
        if self.snelheid < CarAgent.max_snelheid:
            self.snelheid += 1

        return self.snelheid

    def remmen(self):
        self.snelheid -= 1

        return self.snelheid

    def move(self):
        pass

    def Role_of_randomization(self)
        pass: