from re import S


class Cartes:
    def __init__(self, name, mana, description, cout, effet):
        self._name = "card"
        self._mana = mana
        self.description = description
        self.cout = cout
        self.effet = "effet devastateur"
        
        
class Cristal(Cartes):
    def __init__(self, valeur, cout, gainmana):
        self._valeur = valeur
        self._cout = cout
        self._gainmana = gainmana
        
class Creature(Cartes):
    def __init__(self, PV, degats, cout, contre, mort):
        self._PV = PV
        self._degats = degats
        self.cout = cout
        self.contre = contre 
        self.mort = mort
        
class Blast(Cartes):
    def __init__(self, valeur, defausse):
        self.valeur = valeur
        self.degats = valeur
        self.defausse = defausse
        
class Mage:
   def __init__(self, PV, manatot, manaactu, main, defausse, zone, manaregen, attaque, cout): 
       self.PV = PV
       self.manatot = manatot
       self.manaactu = manaactu
       self.main = main
       self.defausse = defausse
       self.zone = zone
       self.manaregen = manaregen
       self.attaque = attaque
       self.cout = cout