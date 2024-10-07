# Boggle-Board-Solver
## Project Overview

This project is a Boggle Board Solver AI that efficiently finds all valid words on a Boggle board using a Trie data structure and recursive backtracking for prefix lookups. The solver can handle boards of various sizes, including larger ones like 50x50.

The AI works by recursively exploring all possible paths on the Boggle board, starting from each letter, to form potential words. It uses the Trie data structure to efficiently check whether the current path forms a valid prefix or word. If the path matches a valid word in the dictionary, it is added to the result. The Trie helps prune invalid paths early, optimizing the search process by avoiding unnecessary exploration of non-existent words.

## Features
* **Customizable Boggle Board:** Define a board of any size (default is 20x20).
* **Optimized Word Search:** Uses a Trie structure for efficient prefix matching.
* **Backtracking Algorithm:** Explores all possible paths recursively with pruning based on Trie prefixes.
* **Dictionary Support:** The solver uses a dictionary file to validate words.
* **Command-Line Interface:** Allows the solver to be run directly from the terminal.

## Setup
To use this solver you just have to clone this repository using one of the following commands.
- Through HTTPS:
`git clone https://github.com/yourusername/boggle-solver.git`
- Through SSH:
`git clone git@github.com:d3xt1le/Boggle-Board-Solver.git`
- Through GitHub CLI:
`gh repo clone d3xt1le/Boggle-Board-Solver`

## Running the solver
1. Navigate to the project directory:
`cd path/to/repository`
2. The repository contains the following components:
    - `Boards/`: A folder containing all the pre-defined Boggle boards that the AI can solve.
    - `Outputs/`: This folder will store the output text files, listing all the validated words the AI has found on the Boggle boards.
    - `board_generator.py`: A Python script to randomly generate NxN Boggle boards. 
    - `boggle_solver.py`: The main script that runs the AI to solve the Boggle boards. This script will search for valid words on the board using the dictionary.
    - `word_dictionary.txt`: A text file containing the dictionary of words used by the AI to validate and identify words found on the board.
3. To generate random boards:
`python board_generator.py <board_size> <output_filename>`
    - The generated board will be saved to the `Outputs/` folder.
4. To run the solver:
`python boggle_solver.py Boards/<board_filename> word_dictionary.txt`

## Key Code Components
1. **Trie Data Structure:**
    - **Purpose:** Efficiently stores and retrieves words from the dictionary, allowing quick prefix checks.
    - **Usage:** 
      - `insert(word)`: Adds words to the Trie.
      - `search(word)`: Checks if a word exists in the Trie.
      - `startWith(prefix)`: Checks if any word in the Trie starts with the given prefix.
2. **Recursive Backtracking(`explorePaths` Function):**
    - **Purpose:** Explores all possible paths on the Boggle Board to form valid words.
    - **Process:**
      - For each starting position on the board, it recursively explores all adjacent cells.
      - Utilizes the Trie to prune paths that cannot lead to valid words (i.e., if the current string isn't a prefix of any word in the dictionary).
      - Collects valid words and avoids revisiting the same cell in a single word path.
