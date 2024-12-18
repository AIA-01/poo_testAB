import math

class TestAB:
    def __init__(self, succes_A, taille_A, succes_B, taille_B, niveau_confiance=1.96):
        self.succes_A = succes_A
        self.taille_A = taille_A
        self.succes_B = succes_B
        self.taille_B = taille_B
        self.z = niveau_confiance

    def calcul_IC(self, succes, taille):
        p = succes / taille
        erreur_standard = math.sqrt(p * (1 - p) / taille)
        return (p - self.z * erreur_standard, p + self.z * erreur_standard)

    def comparer(self):
        IC_A = self.calcul_IC(self.succes_A, self.taille_A)
        IC_B = self.calcul_IC(self.succes_B, self.taille_B)

        print(f"Intervalle de confiance pour Version A : [{IC_A[0]:.2%}; {IC_A[1]:.2%}]")
        print(f"Intervalle de confiance pour Version B : [{IC_B[0]:.2%}; {IC_B[1]:.2%}]")

        if IC_A[1] < IC_B[0]:
            print("La Version B est significativement meilleure que la Version A.")
        elif IC_B[1] < IC_A[0]:
            print("La Version A est significativement meilleure que la Version B.")
        else:
            print("Il n'y a pas de différence significative entre les deux versions.")

# Exemple
test = TestAB(succes_A=40, taille_A=100, succes_B=55, taille_B=100)
test.comparer()