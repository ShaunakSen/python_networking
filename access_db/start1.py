class PatyAnimal:
    x = 0

    def __init__(self):
        print "i am constructed.. i am hungry"

    def party(self):
        self.x += 1
        print 'So far', self.x

    def __del__(self):
        print 'Byee..', self.x


mini = PatyAnimal()

mini.party()
mini.party()
mini.party()

print dir(mini)
print 'program about to end.. '
