![Logo](https://raw.githubusercontent.com/nnisarggada/NyChess/main/Logo.png)

# NyChess

A python Chess Engine and AI

## Technologies Used

NyChess is built using several technologies and algorithms to provide you with an enjoyable chess-playing experience:

### [Pygame](https://www.pygame.org/)

NyChess is developed using the Pygame library, which provides the framework for creating 2D games in Python. Pygame simplifies tasks like rendering graphics, handling user input, and managing game logic, making it an excellent choice for creating interactive chess games.

### Minimax Algorithm

The core of NyChess's AI opponent relies on the [Minimax algorithm](https://en.wikipedia.org/wiki/Minimax). Minimax is a decision-making algorithm used in two-player games, such as chess, to determine the best move for the computer player. It explores the game tree by evaluating possible moves and their outcomes, ultimately selecting the move that minimizes the maximum potential loss.

### Alpha-Beta Pruning

To optimize the Minimax algorithm's performance, NyChess incorporates [Alpha-Beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning). Alpha-Beta pruning is a technique that reduces the number of nodes evaluated in the game tree, making the search more efficient. By eliminating branches of the tree that are known to be suboptimal, Alpha-Beta pruning speeds up the AI's decision-making process.

These technologies and algorithms work together to provide you with a challenging and enjoyable chess-playing experience in NyChess.

## Installation

### Windows

[Install EXE](https://github.com/nnisarggada/NyChess/releases/tag/Windows)

### Linux AppImage

[Install AppImage](https://github.com/nnisarggada/NyChess/releases/tag/Linux)

### Linux Manual Install

Install using the included `install.sh` script or by running the following commands after cloning the repo -

```bash
  cd NyChess
  sudo cp ./NyChess-Linux /usr/bin/
  sudo mkdir ~/.local/share/applications
  sudo cp ./NyChess.desktop ~/.local/share/applications/
  sudo cp NyChess.svg /usr/share/icons/
```

### Linux Manual Uninstalling

Uninstall using the included `uninstall.sh` script or by running the following commands after cloning the repo -

```bash
  sudo rm -rf /usr/bin/NyChess-Linux
  sudo rm -rf ~/.local/share/applications/NyChess.desktop
  sudo rm -rf /usr/share/icons/NyChess.svg
```

## Controls

Press **' m '** to **return to main menu**

Press **' z '** to **undo move**

Press **' f '** to **flip board**
