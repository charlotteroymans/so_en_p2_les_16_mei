from verkiezing import Kandidaat, Stem, Kiezer

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self):
        return f"{self.naam} ({self.opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self.opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.opleiding:
            stem = DecaanStem(kandidaat, self.opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} ({self.opleiding})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")
lijst_DecaanKandidaten = [DecaanKandidaat('Jeffrey','Fysica'),DecaanKandidaat('Stefaan','Fysica'),DecaanKandidaat('Willem','Wiskunde')]
lijst_DecaanKiezers = [DecaanKiezer('Jessica','Wiskunde'),DecaanKiezer('Pablo','Fysica'),DecaanKiezer('Sophie','Fysica')]

for kiezer in lijst_DecaanKiezers:
    for kandidaat in lijst_DecaanKandidaten:
        kiezer.stem(kandidaat)
print('Stemmen per kandidaat:')
for kandidaat in lijst_DecaanKandidaten:
    print(f'{kandidaat}:{len(kandidaat.stemmen)} stemmen')