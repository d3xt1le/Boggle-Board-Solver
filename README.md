# Boggle-Board-Solver
## Project Overview

This project is a Boggle Board Solver AI that efficiently finds all valid words on a Boggle board using a Trie data structure and recursive backtracking for prefix lookups. The solver can handle boards of various sizes, including larger ones like 50x50.

The AI works by recursively exploring all possible paths on the Boggle board, starting from each letter, to form potential words. It uses the Trie data structure to efficiently check whether the current path forms a valid prefix or word. If the path matches a valid word in the dictionary, it is added to the result. The Trie helps prune invalid paths early, optimizing the search process by avoiding unnecessary exploration of non-existent words.