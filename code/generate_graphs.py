import networkx as nx
import matplotlib.pyplot as plt

def generate_random_graph(n, p):
    """ Génère un graphe aléatoire avec n sommets et probabilité p de connexion entre deux sommets """
    G = nx.erdos_renyi_graph(n, p)
    return G

def plot_graph(G, title="Graphe généré"):
    """ Affiche le graphe généré """
    plt.figure(figsize=(6, 6))
    nx.draw(G, with_labels=True, node_color="skyblue", edge_color="gray")
    plt.title(title)
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    G = generate_random_graph(10, 0.3)
    plot_graph(G)

