class Model:
    def __init__(self, nom, datesortie, categorie, typecarburant):
        self.__nom = nom
        self.__datesortie = datesortie
        self.__categorie = categorie
        self.__typecarburant = typecarburant

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nvnom):
        self.__nom = nvnom

    @property
    def datesortie(self):
        return self.__datesortie

    @datesortie.setter
    def datesortie(self, datesortie):
        self.__datesortie = datesortie

    @property
    def categorie(self):
        return self.__categorie

    @categorie.setter
    def categorie(self, categorie):
        self.__categorie = categorie

    @property
    def typecarburant(self):
        return self.__typecarburant

    @typecarburant.setter
    def typecarburant(self, typecarburant):
        self.__typecarburant = typecarburant

    def tostring(self):
        return (
            f"\nMODEL ==> Nom: {self.__nom}"
            f"\nDate Sortie: {str(self.__datesortie)}"
            f"\nCategorie: {self.__categorie}"
            f"\nType Carburant: {self.__typecarburant}\n"
        )

class MaisonVoiture:
    def __init__(self, nom, origine, listemodels=[]):
        self.__nom = nom
        self.__origine = origine
        self.__listemodels = listemodels

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def origine(self):
        return self.__origine

    @origine.setter
    def origine(self, origine):
        self.__origine = origine

    def ajouternvm(self, md):
        self.__listemodels.append(md)

    def supprimermodel(self, nommd):
        for model in self.__listemodels:
            if model.nom == nommd:
                self.__listemodels.remove(model)
                break

    def nombremodels(self):
        return len(self.__listemodels)

    def affichermodels(self):
        for model in self.__listemodels:
            print(model.tostring())

    def nombremodeltypecarburant(self, typecarburant):
        count = 0
        for model in self.__listemodels:
            if model.typecarburant == typecarburant:
                count += 1
        return count

    def nombremodelcategorie(self, categorie):
        count = 0
        for model in self.__listemodels:
            if model.categorie == categorie:
                count += 1
        return count

# Test
model1 = Model("Model1", "2021-01-18", "Sedan", "Essence")
model2 = Model("Model2", "2022-02-01", "SUV", "Diesel")

maison_voiture = MaisonVoiture("MaVoiture", "France", [model1, model2])

maison_voiture.affichermodels()

model3 = Model("Model3", "2022-03-01", "Sedan", "Hybrid")
maison_voiture.ajouternvm(model3)

maison_voiture.supprimermodel("Model1")

maison_voiture.affichermodels()

print("Nombre de modèles:", maison_voiture.nombremodels())
print("Nombre de modèles Diesel:", maison_voiture.nombremodeltypecarburant("Diesel"))
print("Nombre de modèles SUV:", maison_voiture.nombremodelcategorie("SUV"))
