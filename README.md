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
    - The generated board will be saved to the `Boards/` folder.
4. To run the solver:
`python boggle_solver.py Boards/<board_filename> word_dictionary.txt`
    - The found words will be saved to the `Outputs/` folder.

## Board Solver Example:
- Running the solver on a 4x4 board:
`python boggle_solver.py Boards/board4.txt word_dictionary.txt`
- Terminal Output:
```python
Y W A B
Y X I D
Q M D J
P L N A

And we're off!
Running with cleverness ON
All done


Searched total of 205 moves in 0.002262 seconds.


Words found:
2 -letter words: AB, AD, AI, AN, AW, AX, BA, BI, ID, MI, MY, NA, XI
3 -letter words: ADD, AID, AIM, AND, BAD, BID, DAB, DAN, DAW, DIB, DID, DIM, IMP, JIB, MIB, MID, MIX, WAB, WAD, WAX
4 -letter words: JIMP, WADI, WAXY, WIMP
5 -letter words: ADDAX, ADMIX

Found 39 words in total.
Alpha-sorted list words:
AB, AD, ADD, ADDAX, ADMIX, AI, AID, AIM, AN, AND, AW, AX, BA, BAD, BI, BID, DAB, DAN, DAW, DIB, DID, DIM, ID, IMP, JIB, JIMP, MI, MIB, MID, MIX, MY, NA, WAB, WAD, WADI, WAX, WAXY, WIMP, XI
```
- Output file with found words:
```
AB
AD
ADD
ADDAX
ADMIX
AI
AID
AIM
AN
AND
AW
AX
BA
BAD
BI
...
```

## Board Generator Example:
- Running the generator to create a 10x10 board:
`python board_generator.py 10 board10.txt`
- Contents of output file:
```
C X A E D A B B H T
X M D C G R D K H V
O S O I O C B J W W
J Z W X G A X E D V
Y E L L N S B L H R
J N Z W G Y U R X X
C L S Y N N M Z K B
A L Q H F N S U M T
B K T Z O Z B T Q G
F R G Z Z W N J U S
```

## Key Solver Components
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
