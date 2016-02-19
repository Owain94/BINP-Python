class Student:
    def __init__(self, studentnr, naam, woonplaats, leeftijd):
        self.studentnr = studentnr
        self.naam = naam
        self.woonplaats = woonplaats
        self.leeftijd = leeftijd

    def set_studentnr(self, studentnr):
        self.studentnr = studentnr

    def get_studentnr(self):
       return self.studentnr

    def set_naam(self,naam):
        self.naam = naam

    def get_naam(self):
        return self.naam

    def set_woonplaats(self, woonplaats):
        self.woonplaats = woonplaats

    def get_woonplaats(self):
        return self.woonplaats

    def set_leeftijd(self,leeftijd):
        self.leeftijd = leeftijd

    def get_leeftijd(self):
        return self.leeftijd

