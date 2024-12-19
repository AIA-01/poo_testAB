import random
import matplotlib.pyplot as plt

# Simuler les visiteurs
TOTAL_VISITORS = 1_000

def simulate_button_clicks(total_visitors, prob_click_A, prob_click_B):
    """
    Simule les clics des visiteurs sur deux versions de boutons.

    :param total_visitors: Nombre total de visiteurs
    :param prob_click_A: Probabilité de clic pour le bouton A
    :param prob_click_B: Probabilité de clic pour le bouton B
    :return: Nombre de clics pour A et B
    """
    group_A_visitors = total_visitors // 2
    group_B_visitors = total_visitors - group_A_visitors

    clicks_A = sum(random.random() < prob_click_A for _ in range(group_A_visitors))
    clicks_B = sum(random.random() < prob_click_B for _ in range(group_B_visitors))

    return clicks_A, clicks_B

# Définir les probabilités de clic
prob_click_A = 0.25  # 25% probabilité pour "Acheter maintenant"
prob_click_B = 0.30  # 30% probabilité pour "Ajouter au panier"

# Simuler les clics
clicks_A, clicks_B = simulate_button_clicks(TOTAL_VISITORS, prob_click_A, prob_click_B)

# Afficher les résultats
print(f"Version A (Acheter maintenant) : {clicks_A} clics")
print(f"Version B (Ajouter au panier) : {clicks_B} clics")

# Créer le graphique
labels = ['Version A (Acheter maintenant)', 'Version B (Ajouter au panier)']
values = [clicks_A, clicks_B]
colors = ['blue', 'red']

plt.bar(labels, values, color=colors)
plt.title('Comparaison des clics sur les boutons')
plt.ylabel('Nombre de clics')
plt.xlabel('Version du bouton')
plt.show()