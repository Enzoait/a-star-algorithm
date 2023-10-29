# A🌟 Algorithm

## 🇫🇷 (english below)

A🌟 Algorithm est un [algorithme  a*](https://fr.wikipedia.org/wiki/Algorithme_A*) codé en python permettant d'afficher le chemin le plus rapide entre 2 noeuds.

## Installation

```shell
git clone https://github.com/Enzoait/a-star-algorithm
```

```shell
cd a-star-algorithm
```
#### Afficher uniquement le chemin le plus court

```shell
py a_starpathfinder.py 
```

#### Afficher le chemin le plus court ainsi que chaque étape de la recherche du chemin le plus court

```shell
py step_by_step_a_star.py 
```

### Utilisation :

#### Etape 1 :

Définissez votre graphe dans le dictionnaire "graph" de la fonction "transition" comme dans l'exemple çi après :

```py
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
```

#### Etape 2 :

Définissez vos valeurs heuristiques dans le dictionnaire "heuristic_values" de la fonction "h" comme dans l'exemple çi après :

```py
# Définissez vos valeurs heuristiques ici / Define your heuristic values here.
heuristic_values = {0: 4, 1: 2, 2: 2, 3: 2, 4: 1, 5: 3, 6: 4, 7: 0}
```

#### Etape 3 :

Définissez votre noeud de départ et votre noeud à atteindre dans les variables "start_node" et "goal_node" comme dans l'exemple çi après :

```py
# Définissez votre noeud de départ ici / Define your start node here.
start_node = 0 
# Définissez votre noeud d'arrivée ici / Define your goal node here.
goal_node = 7 
```

### Mots clés : 
- [Intelligence Artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) 
- [Algorithme A*](https://fr.wikipedia.org/wiki/Algorithme_A*)
- [Python](https://fr.wikipedia.org/wiki/Python_(langage))

#### Créé par [AIT-YAKOUB Enzo](https://github.com/Enzoait).

## 🇬🇧 

A🌟 Algorithm is a Python coded [a* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) that displays the shortest way between 2 nodes. 

## Installation

```shell
git clone https://github.com/Enzoait/a-star-algorithm
```

```shell
cd a-star-algorithm
```
#### Displays only the shortest way

```shell
py a_starpathfinder.py 
```

#### Displays the shortest way and all the searching steps of the shortest way

```shell
py step_by_step_a_star.py 
```

### Usage :

#### Step 1 :

Define your graph in the "graph" dictionnary of the "transition" function like in the exemple below :

```py
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
```

#### Step 2 :

Define your heuristic values in the "heuristic_values" dictionnary of the "h" fuction like in the exemple below :

```py
# Définissez vos valeurs heuristiques ici / Define your heuristic values here.
heuristic_values = {0: 4, 1: 2, 2: 2, 3: 2, 4: 1, 5: 3, 6: 4, 7: 0}
```

#### Step 3 :

Define your start node and your goal node in the "start_node" and "goal_node" variables like in the exemple below :

```py
# Définissez votre noeud de départ ici / Define your start node here.
start_node = 0 
# Définissez votre noeud d'arrivée ici / Define your goal node here.
goal_node = 7 
```

### Keywords : 
- [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)
- [A* Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

#### Made by [AIT-YAKOUB Enzo](https://github.com/Enzoait).

