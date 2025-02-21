import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def generate_clique(n):
    """ Génère un graphe de type clique avec n sommets. """
    G = nx.complete_graph(n)
    return G

def generate_random_graph(n, p=0.5):
    """ Génère un graphe aléatoire de Erdős-Rényi avec n sommets et probabilité p. """
    G = nx.erdos_renyi_graph(n, p)
    return G

from scipy.spatial import Delaunay

def generate_planar_graph(n):
    points = np.random.rand(n, 2)  # Générer n points aléatoires dans le plan
    tri = Delaunay(points)  # Calcul de la triangulation de Delaunay

    G = nx.Graph()
    for simplex in tri.simplices:
        for i in range(3):  # Un triangle a 3 sommets
            for j in range(i + 1, 3):
                G.add_edge(tuple(points[simplex[i]]), tuple(points[simplex[j]]))

    return G


def plot_graph(G, title="Graphe"):
    """ Affiche le graphe donné. """
    plt.figure(figsize=(6, 6))
    nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
    plt.title(title)
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    G_clique = generate_clique(5)
    plot_graph(G_clique, "Clique (n=5)")
    plt.show()  # 🔥 Forcer l'affichage sur Colab

    G_random = generate_random_graph(5, 0.5)
    plot_graph(G_random, "Graphe Aléatoire (n=5, p=0.5)")
    plt.show()  # 🔥 Forcer l'affichage sur Colab

    G_planar = generate_planar_graph(5)
    plot_graph(G_planar, "Graphe Planaire (n=5)")
    plt.show()  # 🔥 Forcer l'affichage sur Colab
