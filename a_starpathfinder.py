class EmptyOpen(Exception):
    def __init__(self, message="Une erreur s'est produite."):
        self.message = message
        super().__init__(self.message)

# Définir le graphe.
def transition(node):
    graph = {
        0: {1: 3, 2: 1, 3: 1},
        1: {4: 1, 5: 1},
        2: {5: 3, 6: 2},
        3: {6: 1, 7: 6},
        4: {7: 1},
        5: {7: 3},
        6: {7: 5},
        7: {}
    }
    return graph.get(node, []) 

# Définir la fonction heurastique.
def h(node, goal):
    return abs(node - goal)

#Algorithme de recerche dans le graphe, affiche le chemin le plus court vers le noeud "goal", ou "Aucun chemin trouvé vers le noeud goal." si le "goal" est inatteignable.
def rechercheGraph(start, goal):
    open_list = [(start, 0, [])]  # (noeud, coût, path)
    closed = set()

    while open_list:
        node, cost, path = min(open_list, key=lambda x: x[1] + h(x[0], goal))
        open_list.remove((node, cost, path))

        if node == goal:
            path.append(node)
            print("Chemin trouvé:", path)
            break

        closed.add(node)
        for neighbor in transition(node):
            if neighbor not in closed:
                open_list.append((neighbor, cost + 1, path + [node]))

    else:
        raise EmptyOpen("Aucun chemin trouvé vers le noeud goal.")

# Utilisation
start_node = 0
goal_node = 5
rechercheGraph(start_node, goal_node)



