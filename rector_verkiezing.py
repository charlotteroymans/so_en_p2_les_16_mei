from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def __str__(self):
        return f"{self.naam} (Rector: {self.faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.faculteit = faculteit

    def __str__(self):
        return f"Stem op {self.kandidaat} (Rector: {self.faculteit})"
    
lijst_kandidaten = [
    RectorKandidaat("Jean", "Wiskunde"),
    RectorKandidaat("Jef", "Natuurkunde"),
    RectorKandidaat("BOBO", "Scheikunde"),
]

lijst_kiezers = [
    RectorStem("Jiji", "Wiskunde"),
    RectorStem("Lili", "Natuurkunde"),   
    RectorStem("Char", "Scheikunde"),
    RectorStem("Dave", "Wiskunde")
]
print(lijst_kandidaten)
print(lijst_kiezers)
