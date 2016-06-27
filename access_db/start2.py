class PartyAnimal2:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print self.name, 'Constructed'

    def party(self):
        self.x += 1
        print self.name, "party count:", self.x


class FootballFan(PartyAnimal2):
    points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print self.name, "points:", self.points


mini = PartyAnimal2("little mini")
mini.party()

shona = PartyAnimal2("budhhu shona")
shona.party()

paddy = FootballFan("Paddy")
paddy.party()
paddy.touchdown()
