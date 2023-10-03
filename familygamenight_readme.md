# Family Game Night Program

## Description
The Family Game Night program allows you to manage your family's game inventory. You can add new games, select random games to play, view game details, and more. If your family has ever argued over which game to play or you have found yourself playing the same games over and over and want to find out how to get a bigger variety of games to the table, this will make your family game night much simpler.

## Features
- Create a new game list
- Add new games to the existing list
- Randomly select a game for playing
- Display game details by game
- Display a list of games available to play
- Display game details for all games
- Clear lists (game list, played games, and game details)

## Usage
1. Run the program.
2. Choose from the available options to manage your game inventory.
3. Follow the on-screen prompts to add games, select games to play, and view game details.

## Requirements
- Python 3.11
- Libraries: random, pickle, tabulate, textwrap, webbrowser

## How to Run
1. Install Python 3.11 if you haven't already.
2. Install the required libraries using pip:
	pip install tabulate
3. Run the program:
	python main.py
4. Upon running the program for the first time, it will automatically create two files, `games.txt` and `played_games.txt`, if they don't already exist. These files store your game list and played games list, respectively. You can add or modify games directly in these files by typing games one on each line, and the program will read and update them accordingly.


## Author
Marcia Hope

## Acknowledgments
- Special thanks to [Tabulate](https://pypi.org/project/tabulate/) for the table formatting library.
- Inspired by the many arguments that ensue when choosing games for family game night.

