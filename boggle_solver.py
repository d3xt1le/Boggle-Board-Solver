# library imports
import os
import time
import random
import string
from sys import argv

# global variables
totalMoves = 1
SUBGROUP_DEPTH = 2


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEndOfWord

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def examineState(myBoard, position, path):
    # go through board to get individual letter from path
    newPath = path + [position]
    possible_word = "".join([getLetter(myBoard, position)
                            for position in newPath])

    # check for created word in dictionary
    return possible_word


def explorePaths(myBoard, trie, currentPos, path, wordList):
    # Get possible moves around currentPosition
    possible_moves = possibleMoves(currentPos, myBoard)

    # Get legal moves
    legal_moves = legalMoves(possible_moves, path + [currentPos])

    # Recurse through legal moves
    for nextCoord in legal_moves:

        # Get state of found word
        newStr = examineState(myBoard, nextCoord, path + [currentPos])

        # Check if current string is a valid prefix in the Trie
        if trie.startsWith(newStr):

            # Check if the current string forms a valid word
            if trie.search(newStr):
                word_len = len(newStr)

                # create list for words of the same length
                if word_len not in wordList:
                    wordList[word_len] = []

                # Add word to list if not already in list
                if newStr not in wordList[word_len]:
                    wordList[word_len].append(newStr)

            # Recurse further if it can still form longer words
            global totalMoves
            totalMoves += 1
            explorePaths(myBoard, trie, nextCoord,
                         path + [currentPos], wordList)

    return totalMoves


def getLetter(board, position):
    # get letter at given position
    xCoord, yCoord = position
    return board[xCoord][yCoord]


def legalMoves(moves, path):
    # get legal moves
    return [move for move in moves if move not in path]


def loadBoard(filename):
    # load board
    return [line.split() for line in open(filename)]


def printBoard(boardObj):
    # display NxN board
    [print(*letter) for letter in boardObj]


def possibleMoves(xyPair, boardObj):
    # initialize variables
    OFFSETS = [-1, 0, 1]
    currentPos = xyPair
    boardSize = len(boardObj)

    # get offset coordinates
    offsetCoords = [(xOff, yOff)
                    for xOff in OFFSETS for yOff in OFFSETS if xOff != 0 or yOff != 0]

    # get surrounding coordinates to current position
    adjacentCoords = [list(offset + pos for offset, pos in zip(xyOffset, currentPos)
                      if pos >= 0 and pos < boardSize) for xyOffset in offsetCoords]

    # get rid of illegal moves
    possibleMoves = [tuple(coord) for coord in adjacentCoords if all(
                     elem >= 0 and elem < boardSize for elem in coord)]

    # return possible moves
    return possibleMoves


def readDictionary(filename):
    # Initialize the Trie
    trie = Trie()

    # Load the dictionary and insert words into the Trie
    for word in open(filename):
        word = word.strip().upper()
        trie.insert(word)

    return trie


def runBoard(board_filename, dictionary_filename):
    # Load the board and dictionary
    myBoard = loadBoard(board_filename)
    myTrie = readDictionary(dictionary_filename)

    # Initialize variables
    BOARD_SIZE = len(myBoard)
    wordList = {}
    path = []

    # Display board
    printBoard(myBoard)
    print("\nAnd we're off!\nRunning with cleverness ON\nAll done\n")

    # Start time
    startTime = time.time()

    # Loop through the board
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            currentPos = (row, col)  # get current board position

            # calculate total moves made while exploring the board
            totalMoves = explorePaths(
                myBoard, myTrie, currentPos, path, wordList)

    # End time
    endTime = time.time()

    # Display times and moves
    print(
        f"\nSearched total of {totalMoves} moves in {round(endTime - startTime, 6)} seconds.\n")

    # Display organized words
    print("\nWords found:")
    for key, value in sorted(wordList.items()):
        print(f"{key} -letter words: ", end='')
        print(*sorted(value), sep=', ')

    # Create list of words
    wordList = [word for wordGroup in list(
        wordList.values()) for word in wordGroup]

    # Get total words in list
    totalWords = len(wordList)

    # Print all words in alpha sorted list
    print(f"\nFound {totalWords} words in total.\nAlpha-sorted list words:")
    print(*sorted(wordList), sep=', ')

    return wordList


def outputFile(boardFile, wordList):
    # check output directory exists
    output_dir = "Outputs"
    os.makedirs(output_dir, exist_ok=True)

    # get file name from path
    filename = os.path.basename(boardFile)

    # create output file name
    outName = os.path.join(
        output_dir, filename.replace(".txt", "") + "_words.txt")

    # open output file and write words to it
    with open(outName, "w") as outFile:
        for word in wordList:
            outFile.write(f"{word.upper()}\n")


def main():
    # assign argv arguments
    _, boardArg, dictionaryArg = argv
    board_filename = boardArg
    dictionary_filename = dictionaryArg

    # add list of words to output file
    wordList = runBoard(board_filename, dictionary_filename)
    wordList.sort()
    outputFile(board_filename, wordList)


if __name__ == "__main__":
    main()
