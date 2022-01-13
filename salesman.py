#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:51:25 2022

@author: badawe
"""

#Cette fonction renvoie le chemin le plus court dans le graphe passant par tous les nœuds
def travellingSalesman (graph, sourceNode) :

    # Nous stockons le meilleur chemin ici

    bestLength = float("inf")
    bestPath = None

    # Ainsi la fonction prend en argument les nœuds qui ne sont pas encore visités, le graphe et un emplacement courant
    # De plus, on se souvient du chemin actuellement croisé et du poids associé
    # Fondamentalement, nous effectuons une recherche en profondeur d'abord et étudions la longueur du chemin s'il contient tous les nœuds

    def exhaustive (remainingNodes, currentNode, currentPath, currentLength, graph) :
        
        # S'il ne reste aucun nœud, nous avons un chemin comprenant tous les nœuds
        # Nous l'enregistrons comme le meilleur s'il est meilleur que le meilleur actuel
        if not remainingNodes :
            print("Found Hamiltonian path", repr(currentPath), "of size", currentLength)
            nonlocal bestLength, bestPath
            if currentLength < bestLength :
                bestLength = currentLength
                bestPath = currentPath
        
        # S'il reste des nœuds, nous effectuons une recherche en profondeur d'abord
        # On augmente le chemin et sa longueur dans l'appel récursif
        # Évidemment, nous ne considérons que les nœuds qui sont accessibles
        else :
            for neighbor, weight in graph[currentNode] :
                if neighbor in remainingNodes :
                    otherNodes = [x for x in remainingNodes if x != neighbor]
                    exhaustive(otherNodes, neighbor, currentPath + [neighbor], currentLength + weight, graph)
    
    #Nous initions la recherche à partir du nœud source

    otherNodes = [x for x in range(len(graph)) if x != sourceNode]
    exhaustive(otherNodes, sourceNode, [sourceNode], 0, graph)
    
    # On retourne le résultat

    return (bestPath, bestLength)

###################################################################
 
# Test de graphe
graph = [[(1, 1), (2, 7), (5, 3)], [(0, 1), (2, 1), (5, 1)], [(0, 7), (1, 1)], [(4, 2), (5, 2)], [(3, 2), (5, 5)], [(0, 3), (1, 1), (3, 2), (4, 5)]]
(result, length) = travellingSalesman(graph, 0)
print(repr(result))
print("La taille du chemin de tous les nœuds la plus faible obtenue est :  ",length)
