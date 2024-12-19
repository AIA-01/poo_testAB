import math

"""
Bien vérifier que vous avez un échantillon aléatoire.
Les proportions seraient par exemple calculer sur un échantillon de 100 ou 1_000 personnes
Puis on calcule l'intervalle de confiance pour chacune des mesures.
"""


def calculate_confidence_interval(n, p, z = 1.96):
    """
    Calcule l'intervalle de confiance pour un taux de conversion donné.

    :param n: Nombre total de visiteurs
    :param p: Taux de conversion observé (actions/visiteurs)
    :param z: Score Z correspondant au niveau de confiance (par défaut 1.96 pour 95%)
    :return: Tuple contenant le taux de conversion et l'intervalle [min, max]
    """
    margin_of_error = z * math.sqrt((p * (1 - p)) / n)
    return p, (p - margin_of_error, p + margin_of_error)


# Données de l'exemple
n_A = 1000
p_A = 0.12
n_B = 1000
p_B = 0.14

# Calcul des intervalles de confiance
confidence_A = calculate_confidence_interval(n_A, p_A)
confidence_B = calculate_confidence_interval(n_B, p_B)

# Affichage des résultats
print(f"Version A : Conversion = {confidence_A[0]:.2%}, Intervalle de confiance = [{
      confidence_A[1][0]:.2%}, {confidence_A[1][1]:.2%}]")
print(f"Version B : Conversion = {confidence_B[0]:.2%}, Intervalle de confiance = [{
      confidence_B[1][0]:.2%}, {confidence_B[1][1]:.2%}]")
