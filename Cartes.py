class Cartes:
    def __init__(self, name, mana, description, cout, effet):
        self._name = "card"
        self._mana = mana
        self.description = description
        self.cout = cout
        self.effet = "effet devastateur"
        
        
class Cristal(Cartes):
    def __init__(self, valeur, cout, gain):
        self._valeur = valeur
        self._cout = cout
        self._managain = gainmana
        
        def gainmana(self, manatot, manaactu):
            manatot+=1
            manaactu+=self._managain
            return manatot, manaactu #regenere et augmente de 1 la reserve de mana
            
        
class Creature(Cartes):
    def __init__(self, PV, degats, cout, contre, mort):
        self._PV = PV
        self._degats = degats
        self.cout = cout
        self.contre = contre 
        self.mort = mort
        
        def infligedegats(self, ciblepv, cibledefense):
            
        
class Blast(Cartes):
    def __init__(self, valeur, defausse):
        self.valeur = valeur
        self.degats = valeur
        self.defausse = defausse
        
class Mage:
   def __init__(self, PV, manatot, manaactu, main, defausse, zone, manaregen, attaque, cout, tour): 
       self.PV = PV
       self.manatot = manatot #mana maximal du joueur avec les cristaux, il augmente de 1 à chaque tour
       self.manaactu = manaactu
       self.main = main
       self.defausse = defausse
       self.zone = zone
       self.manaregen = manaregen
       self.attaque = attaque
       self.cout = cout
       self.tour = tour
def playcard():
    return "card"
def manaregen():
    return manaregen
        #regeneration à chaque tour

def posecreature():
    #pose une creature puis amorce l'offensive