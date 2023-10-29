class EmptyOpen(Exception):
    def __init__(self, message="Aucun chemin trouvé vers le nœud goal."):
        self.message = message
        super().__init__(self.message)

def transition(node):
    # Définissez votre graphe ici / Define your graph here.
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
    return graph.get(node, {})

def h(node, goal):
    # Définissez vos valeurs heuristiques ici / Define your heuristic values here.
    heuristic_values = {0: 4, 1: 2, 2: 2, 3: 2, 4: 1, 5: 3, 6: 4, 7: 0}
    return heuristic_values[node]

#Algorithme de recerche dans le graphe, affiche le chemin le plus court vers le noeud "goal", ou "Aucun chemin trouvé vers le noeud goal." si le "goal" est inatteignable..
def rechercheGraph(start, goal):
    open_list = [(start, 0, [], 0, None)]  # (noeud, coût, path, f(n), parent)
    closed = set()

    while open_list:
        print("open:", [(node, fn, parent) for node, _, _, fn, parent in open_list])
        print("closed:", closed)
        node, cost, path, fn, parent = min(open_list, key=lambda x: x[3])
        open_list.remove((node, cost, path, fn, parent))

        if node == goal:
            path.append(node)
            print("Chemin trouvé:", path, "open:", open_list, "closed:", closed)
            break

        closed.add(node)
        for neighbor, edge_cost in transition(node).items():
            if neighbor not in closed:
                gn = cost + edge_cost
                fn = gn + h(neighbor, goal)
                open_list.append((neighbor, gn, path + [node], fn, node))

    else:
        raise EmptyOpen()

# Utilisation
start_node = 0 # Définissez votre noeud de départ ici / Define your start node here.
goal_node = 7 # Définissez votre noeud d'arrivée ici / Define your goal node here.
rechercheGraph(start_node, goal_node)
