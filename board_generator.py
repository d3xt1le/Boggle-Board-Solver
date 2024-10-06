import os
import sys
import string
import random


def create_boggle_board(size, output_file):
    """Generates a random Boggle board of given size and writes it to a file."""
    charlist = string.ascii_uppercase

    # Ensure the output directory exists
    output_dir = "Boards"
    os.makedirs(output_dir, exist_ok=True)

    # Create the full output file path
    output_path = os.path.join(output_dir, output_file)

    # write character to the output file
    with open(output_path, 'w') as out:
        for _ in range(size):
            line = ' '.join(random.choices(charlist, k=size))
            out.write(line + "\n")

    print("Boggle board created successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <N> <outFile>")
        sys.exit(1)

    script_py, board_size, outFile = sys.argv
    try:
        SIZE = int(board_size)
        create_boggle_board(SIZE, outFile)
    except ValueError:
        print("Please provide a valid integer for the board size.")
        sys.exit(1)
