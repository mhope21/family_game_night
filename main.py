import random
import pickle
from tabulate import tabulate
import textwrap
import webbrowser


# Function to load the game list from the file
def load_game_list(filename):
    try:
        with open(filename, 'r') as gameFile:
            gameData = gameFile.read()
            return [item.strip() for item in gameData.split("\n") if item.strip()]
    except FileNotFoundError:
        return []


# Function to load the game details dictionary from a file
def load_game_details(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist


# Function to save the game list to the file
def save_game_list(filename, gameList):
    with open(filename, 'w') as file:
        for item in gameList:
            file.write(item + "\n")


# Function to save the game details dictionary to a file
def save_game_details(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


# Function to make a new game list
def option1():
    newGameList = []

    for game in range(100):
        availGames = input("Add an available game to your list or type 'Done' to exit: ")

        if availGames.lower() == "done":
            break
        else:
            # Check if the game already exists in newGameList
            if availGames in newGameList:
                print("This game is already on the list.")
            else:
                newGameList.append(availGames)

    if newGameList:  # Only update the game list if newGameList is not empty
        availableGames.clear()  # Clear old list
        erase_game_details('game_details.pickle')

        # Extend the old availableGames list with the newGameList
        availableGames.extend(newGameList)

        save_game_list('games.txt', availableGames)  # Save the updated game list

        # Call a separate function to add descriptions, playtimes, and player counts
        add_game_details(newGameList)


# Function to add games to your existing list
def option2():
    addGameList = []
    for game in range(100):
        availGames = input("Add an available game to your list or type 'Done' to exit: ")

        if availGames.lower() == "done":
            break
        else:
            # Check if the game already exists in available games or played games
            if availGames in availableGames or availGames in playedGames:
                print("This game is already on the list.")
            else:
                addGameList.append(availGames)

    if addGameList:  # Only update the game list if addGameList is not empty
        availableGames.extend(addGameList)  # Update the game list with the new games
        save_game_list('games.txt', availableGames)  # Save the updated game list

        # Run the function to allow user to add game details
        add_game_details(addGameList)


# Function to select a random game to play
def option3():
    if not availableGames:
        print("Your game list is empty.")

        user_choice = input("Do you want to add new games (A) or refresh with played games (R)? ").lower()

        if user_choice == "a":

            # Automatically select option 1 for the user to add new games
            option1()

        elif user_choice == "r":

            if not playedGames:
                print("Your played games list is also empty. Please start a new game list.")

                option1()

            else:
                reset_available_games()

        else:
            print("Invalid choice. Please enter 'A' to add new games or 'R' to refresh with played games.")

    else:

        # Select a random game from the game inventory
        random_game = random.choice(availableGames)

        print("\nI will now choose a random game from your family's game inventory.")

        print("\nYour randomly chosen game for tonight is: " + random_game + ". Enjoy your family game night!\n\n")

        # Add the selected game to played games list and remove from available games
        playedGames.append(random_game)
        availableGames.remove(random_game)

        save_game_list('played_games.txt', playedGames)
        save_game_list('games.txt', availableGames)
        # Save the game details dictionary
        save_game_details('game_details.pickle', game_details)


# Function to show game details by game name
def option4():
    if not availableGames:
        print("Your game list is empty. Please add games to the list first.")
    else:
        try:
            option5()
            game_number = int(input("Enter the number of the game to view its details: "))
            if 1 <= game_number <= len(availableGames):
                selected_game = availableGames[game_number - 1]
                game_info = game_details.get(selected_game, "No description available.")
                print(f"Details for '{selected_game}':\n")

                # Wrap the description text to a maximum width of 125 characters
                wrapped_description = textwrap.fill(game_info.get('description', ''), width=125)

                # Display the selected game's details as a grid table without row categories
                table_data = [
                    ("Description", wrapped_description),
                    ("Playtime", game_info.get('playtime', '')),
                    ("Players", game_info.get('players', '')),
                    ("Web Link", game_info.get('weblink', 'No link available'))
                ]
                print(tabulate(table_data, tablefmt="grid"))

                # Check if a web link exists and open it in a web browser
                web_link = game_info.get('weblink', '')
                if web_link and web_link != 'No link available':
                    decision = input("Do you want to open the web link? (Y/N): ").strip().lower()
                    if decision == 'y':
                        webbrowser.open(web_link)  # Open the web link
            else:
                print("Invalid game number. Please enter a valid game number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function to print games in inventory
def option5():
    print("++++++++++++++++++++ GAME INVENTORY ++++++++++++++++++++")
    for i, game in enumerate(availableGames, 1):
        print(f"{i}. {game}")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def option6():
    if not game_details:
        print("There are no games in the list.")
    else:
        # Assuming game_details is your game details dictionary
        data = [(game, details.get('description', ''), details.get('playtime', ''), details.get('players', '')) for game, details in game_details.items()]

        # Display as a table
        table_headers = ["Game Name", "Description", "Playtime", "Players"]
        print(tabulate(data, headers=table_headers, tablefmt="grid", colalign=("left", "left", "left", "left")))


# Clear the file contents
def erase_file_contents(filename):
    try:
        with open(filename, 'w') as file:
            # Truncate the file to remove all its contents
            file.truncate(0)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


# Function to clear dictionary
def erase_game_details(pickle_filename):
    try:
        # Clear the dictionary
        game_details = {}

        # Open the pickle file in write mode and overwrite it with the empty data
        with open(pickle_filename, 'wb') as file:
            pickle.dump(game_details, file)
    except FileNotFoundError:
        print(f"File '{pickle_filename}' not found.")


# Function to add descriptions, playtimes, and player counts for each game
def add_game_details(game_list):
    for game in game_list:
        gameDescription = input(f"Enter a short description for '{game}' (optional): ")
        gamePlaytime = input(f"Enter the estimated playtime for '{game}' (optional): ")
        playerCount = input(f"Enter the number of players for '{game}' (optional): ")
        webLink = input(f"Enter the link to game instructions for '{game}' (optional): ")

        # Add the details to a dictionary under the game name as the key
        game_details[game] = {'description': gameDescription, 'playtime': gamePlaytime, 'players': playerCount, 'weblink': webLink}
    # Save the game details dictionary
    save_game_details('game_details.pickle', game_details)


# Function to reset availableGames from playedGames
def reset_available_games():
    global availableGames  # Access the global variable

    print("Resetting available games from played games.")
    availableGames.extend(playedGames)  # Move games from playedGames to availableGames
    playedGames.clear()  # Clear the playedGames list

    # Remove the games from the played_games.txt file
    save_game_list('played_games.txt', [])

    # Append the moved games to the games.txt file
    save_game_list('games.txt', availableGames)


# Load the game list
availableGames = load_game_list('games.txt')
playedGames = load_game_list('played_games.txt')

# Load the game details dictionary at the beginning of the program
game_details = load_game_details('game_details.pickle')


# Game Menu
while True:
    print("Choose an option:")
    print("1. Create a new game list")
    print("2. Add new games to the existing list")
    print("3. Randomly select a game for playing")
    print("4. Display game details by game")
    print("5. Display list of games available to play")
    print("6. Display game details (all games)")
    print("7. Clear lists")
    print("8. Exit")

    choice = input()

    if choice == "1":
        option1()

    elif choice == "2":
        option2()

    elif choice == "3":
        option3()

    elif choice == "4":
        option4()

    elif choice == "5":
        option5()

    elif choice == "6":
        option6()

    elif choice == "7":
        erase_file_contents('games.txt')
        erase_file_contents('played_games.txt')
        erase_game_details('game_details.pickle')

        availableGames = []  # Clear the availableGames list
        playedGames = []  # Clear the playedGames list
        game_details = {}  # Clear the game details

    elif choice == "8":
        print("Exiting the game selection menu.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
